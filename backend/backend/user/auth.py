import jwt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from utils.jwt import generate_tokens, decode_token
import json
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def login_auth(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    data = json.loads(request.body.decode())

    email = data.get("email")
    password = data.get("password")

    user = authenticate(request, email=email, password=password)
    if user is None:
        return JsonResponse({"detail": "Invalid email or password"}, status=401)

    user.last_login = now()
    user.save()

    access, refresh = generate_tokens(user.id)
    return JsonResponse({"access": access, "refresh": refresh, "username": user.username})


@csrf_exempt
def refresh_token(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    data = json.loads(request.body.decode())
    refresh_token = data.get("refresh")

    try:
        payload = decode_token(refresh_token)
        if payload.get("type") != "refresh":
            return JsonResponse({"detail": "Invalid token type"}, status=401)

        user_id = payload.get("user_id")
        access, new_refresh = generate_tokens(user_id)
        return JsonResponse({"access": access, "refresh": new_refresh})

    except jwt.ExpiredSignatureError:
        return JsonResponse({"detail": "Refresh token expired"}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"detail": "Invalid refresh token"}, status=401)
