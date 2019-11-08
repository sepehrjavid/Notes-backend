from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
