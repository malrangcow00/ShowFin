from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(User, related_name='like_articles')
    # hashtags = models.ManyToManyField(Hashtag, related_name='articles', blank=True)

    def __str__(self):
        return f'{self.id}: {self.title}'