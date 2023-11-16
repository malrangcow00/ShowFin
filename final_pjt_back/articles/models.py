from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    category = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cateory}: {self.title} by {self.user}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.article.pk}: {self.user} commented'