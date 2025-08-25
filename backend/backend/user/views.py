import json, jwt
from django.http import JsonResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from .models import Post
# from utils.jwt import generate_tokens, decode_token
from utils.jwt_authorize import jwt_required
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    data = json.loads(request.body.decode())
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return JsonResponse({"detail": "All fields required"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"detail": "Username already exists"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)

    return JsonResponse({"id": user.id, "username": user.username, "email": user.email}, status=201)

    


@csrf_exempt
@jwt_required
def create_post(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body.decode())
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return JsonResponse({"detail": "Title and content are required"}, status=400)
        user = User.objects.get(username=data.get("author"))
        post = Post.objects.create(
            title=title,
            content=content,
            author=user,  
        )

        return JsonResponse({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": user.username,
            "created_at": post.created_at,
        }, status=201)

    except Exception as e:
        return JsonResponse({"detail": str(e)}, status=400)

@csrf_exempt
@jwt_required
def update_post(request, post_id):
    if request.method != "PUT":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"detail": "Post not found"}, status=404)

    # Check ownership
    if post.author != request.user:
        return JsonResponse({"detail": "Not authorized"}, status=403)

    data = json.loads(request.body.decode())
    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)
    post.save()

    return JsonResponse({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "updated_at": post.updated_at,
    })

@csrf_exempt
def get_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"detail": "Post not found"}, status=404)

    return JsonResponse({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
    })


@csrf_exempt
@jwt_required
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"detail": "Post not found"}, status=404)

    # Check ownership
    if post.author != request.user:
        return JsonResponse({"detail": "Not authorized"}, status=403)

    post.delete()
    return JsonResponse({"detail": "Post deleted successfully"})


@csrf_exempt
def get_all_posts(request):
    posts = Post.objects.all()
    return JsonResponse([{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author.username,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
    } for post in posts], safe=False)