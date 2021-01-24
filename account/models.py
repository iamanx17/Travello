from django.db import models

# Create your models here.
class userdata(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.username
