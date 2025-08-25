from django.http import JsonResponse
from utils.jwt import decode_token
import jwt

def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"detail": "Authorization header missing"}, status=401)

        token = auth_header.split(" ")[1]

        try:
            payload = decode_token(token)
            if payload.get("type") != "access":
                return JsonResponse({"detail": "Invalid token type"}, status=401)

            request.user_id = payload.get("user_id")  # attach user_id for later use

        except jwt.ExpiredSignatureError:
            return JsonResponse({"detail": "Access token expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"detail": "Invalid token"}, status=401)

        return view_func(request, *args, **kwargs)
    return wrapper
