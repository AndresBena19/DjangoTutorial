from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    secret_question = models.CharField(max_length=300,default="what is you user?")
    secret_answer = models.CharField(max_length=300, default="")

