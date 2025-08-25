from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Admin

from user.forms import UserChangeForm, UserCreationForm
from user.models import User, Post,RequestLog



class UserAdmin(Admin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "email",
        "is_superuser",
        "is_active",
        "is_email_verified",
    ]
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "username",

                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "is_email_verified",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "is_email_verified",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(RequestLog)
