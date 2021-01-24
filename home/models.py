from django.db import models

# Create your models here.

class destination(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    image=models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.name
