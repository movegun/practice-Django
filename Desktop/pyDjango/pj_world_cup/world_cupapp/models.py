from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    pwd = models.CharField(max_length=128)
    username = models.CharField(max_length=128)    
    rdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id
    