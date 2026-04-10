from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)
    vote_limit = models.IntegerField(null=True, blank=True)
    is_unlimited = models.BooleanField(default=False)
    is_named = models.BooleanField(default=False)  # ← 여기 추가

    def __str__(self):
        return self.name

class VoteItem(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# 🔹 사용자별 투표 기록
class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_item = models.ForeignKey(VoteItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.vote_item.title}"