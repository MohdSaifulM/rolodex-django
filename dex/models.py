from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    contact = models.CharField(max_length=15)
    image_url = models.ImageField(default="default-profile-picture1.jpg")

    #created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
