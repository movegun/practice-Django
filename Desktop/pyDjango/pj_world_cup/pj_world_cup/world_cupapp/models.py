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
    
class Ranking(models.Model):
    name = models.CharField(max_length=200)
    rank = models.PositiveIntegerField(default=0)
    def __str__(self):
        return (self.name)
    def update_rank(self):
        self.rank = self.rank +1
        self.save()
        
class All_url(models.Model):
    theme = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.TextField()
    win_num = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.theme+" "+self.name
    def update_win_num(self):
        self.win_num = self.win_num +1
        self.save()

class Comment_test(models.Model):
    comment_num = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    comment = models.TextField()
    hit_num = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
    def update_hit_num(self):
        self.hit_num = self.hit_num +1
        self.save()