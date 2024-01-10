from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Fiction')
    description = models.TextField(max_length=500)
    published_year= models.IntegerField()
    
    def __str__(self):
        return self.title