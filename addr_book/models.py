from django.db import models

# Create your models here.

class author(models.Model):
    AuthorID=models.CharField(primary_key=True, max_length=30)
    Name=models.CharField(max_length=30)
    Age=models.CharField(max_length=30)
    Country=models.CharField(max_length=30)
    
class book(models.Model):
    Title=models.CharField(max_length=30)
    Author=models.ForeignKey(author)
    Publisher=models.CharField(max_length=30)
    PublishDate=models.CharField(max_length=30)
    Price=models.CharField(max_length=30)
    ISBN=models.CharField(primary_key=True, max_length=30)
