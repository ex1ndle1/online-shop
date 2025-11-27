from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
 ######i've added only phone field, because my class enhanced other fields such as email etc. from AbstractUser
    def __str__(self):
        return self.username