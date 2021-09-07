from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

# Create your models here.
class Pic(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    author=models.CharField(max_length=30)
    category=models.ForeignKey('Category',on_delete=CASCADE)
    location=models.ForeignKey('Location',on_delete=CASCADE)
    posted=models.DateField(auto_now=True)
    image= CloudinaryField('image')
    def __str__(self):
        return self.title
    def save_image(self):
        self.save()
        
   
class Location(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
  
        
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
   