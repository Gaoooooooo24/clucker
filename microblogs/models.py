from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
    max_length = 30,
    unique = True,
    validators = [RegexValidator(
        regex = r'^@\w{3,}$',
        message = 'username must consist of @ follow by at least three alphanumericals')]
    )
    bio = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length = 280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


# Create your models here.
