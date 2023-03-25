from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_aat = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title}: {self.content[:50]}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    