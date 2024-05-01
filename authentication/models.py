from django.contrib.auth.models import AbstractUser


class NoirNookUser(AbstractUser):
    def __str__(self):
        if not self.username:
            return f"{self.first_name} {self.last_name}"
        return self.username
