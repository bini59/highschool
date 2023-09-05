from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성될 때만
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다

    def __str__(self):
        return self.title