from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, password, first_name, last_name):
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(
            phone=phone,
            is_staff=False,
            is_superuser=False,
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password):
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(
            phone=phone,
            is_staff=True,
            is_superuser=True,
            )
        user.set_password(password)
        user.save()
        return user
