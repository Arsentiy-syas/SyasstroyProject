from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default='image/profile/avatar_photo.jpg', upload_to='image/profile')