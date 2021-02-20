from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

class PhoneAuthBackend(BaseBackend):
    def authenticate(self, phone=None, password=None):
        user = User.objects.get(phone=phone)
        if user is not None:
            '''
            пароли нужно проверять именно так, а не ==, потому что они зашифрованы
            в базе и простое сравнение с вводом пользователя вернёт false
            '''
            if user.check_password(password) is True:
                return user
            else:
                return None
            return None

    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
