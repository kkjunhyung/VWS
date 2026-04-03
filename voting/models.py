from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)
    vote_limit = models.IntegerField(null=True, blank=True)
    is_unlimited = models.BooleanField(
        default=False,
        verbose_name="투표수 제한 없음"
    )  

    def __str__(self):
        return self.name


class VoteItem(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title