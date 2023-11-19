from django.db import models
from django.contrib.auth import get_user_model
# from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 추가기능 -> 좋아요 갯수 조회 및 좋아요
    like_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(get_user_model(), related_name='liked_articles', blank=True)

    def __str__(self):
        return f'{self.category}: {self.title} by {self.user}'


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 추가기능 -> 좋아요 갯수 조회 및 좋아요
    like_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(get_user_model(), related_name='liked_comments', blank=True)

    def __str__(self):
        return f'{self.article.pk}: {self.user} commented'