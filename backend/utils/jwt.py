import jwt
import datetime
from django.conf import settings


def generate_tokens(user_id: int):
    now = datetime.datetime.now(datetime.timezone.utc)

    access_payload = {
        "user_id": user_id,
        "type": "access",
        "exp": now + settings.JWT_ACCESS_TOKEN_LIFETIME,
        "iat": now,
    }
    refresh_payload = {
        "user_id": user_id,
        "type": "refresh",
        "exp": now + settings.JWT_REFRESH_TOKEN_LIFETIME,
        "iat": now,
    }

    access_token = jwt.encode(access_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return access_token, refresh_token


def decode_token(token: str):
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
