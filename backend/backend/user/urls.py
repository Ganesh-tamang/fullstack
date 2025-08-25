from django.urls import path
from user import auth, views

urlpatterns = [
    path("login/", auth.login_auth, name="login"),
    path("refresh/", auth.refresh_token, name="refresh"),
    path("register/", views.register_view, name="register"),
    path("posts/create", views.create_post, name="create-post"),
    path("posts/<int:post_id>", views.get_post, name="get-post"),
    path("posts/<int:post_id>/delete", views.delete_post, name="delete-post"),
    path("posts/", views.get_all_posts, name="get-all-posts"),
]