from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    docstring
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
