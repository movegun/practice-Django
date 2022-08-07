from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    pwd = models.CharField(max_length=128)
    username = models.CharField(max_length=128)    
    rdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id

class Comment_room(models.Model):
    keyword = models.CharField(max_length=200)
    def __str__(self):
        return (self.id, self.keyword)

class Brand_member(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    name = models.CharField(max_length=200)
    url = models.TextField()
    def __str__(self):
        return self.name
    
class Urls(models.Model):
    name = models.CharField(max_length=200)
    url = models.TextField()
    def __str__(self):
        return self.name