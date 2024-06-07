from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

User = get_user_model()


class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    last_name = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    wallet_address = models.CharField(max_length=42, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Adding related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Adding related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Hub(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paragraph_name = models.CharField(max_length=500)
    image_url = models.URLField(max_length=500)
    text_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.paragraph_name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)