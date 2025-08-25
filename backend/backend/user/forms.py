from django.contrib.auth.forms import UserChangeForm as ChangeForm
from django.contrib.auth.forms import UserCreationForm as CreationForm

from user.models import User


class UserCreationForm(CreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "is_active",
            "is_superuser",
            "is_staff",
            "is_email_verified",
        )


class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "is_active",
            "is_superuser",
            "is_staff",
            "is_email_verified",
        )
