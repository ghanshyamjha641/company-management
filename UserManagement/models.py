from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'custom_user'  # 👈 your desired table name

    def __str__(self):
        return self.username
