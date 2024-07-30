from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return f"USER[ username:{self.get_username()} email:{self.email} ]"
