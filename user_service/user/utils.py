import jwt
import datetime
import logging

from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from .models import User

logger = logging.getLogger(__name__)  # Properly configure logger

def decode_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        user_id = payload.get('id')
        user = User.objects.get(id=user_id)
        return user
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')
    except User.DoesNotExist:
        raise AuthenticationFailed('User not found')


def create_token(user):
    try:
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow()
        }
        return jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    except Exception as e:
        logger.error(f"Token generation error: {str(e)}")
        raise
