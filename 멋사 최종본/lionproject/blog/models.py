from functools import wraps
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    write = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]