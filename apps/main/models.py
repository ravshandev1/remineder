from django.db import models
from user.models import User


class Post(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    @property
    def like(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    post = models.ForeignKey(Post, models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    post = models.ForeignKey(Post, models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
