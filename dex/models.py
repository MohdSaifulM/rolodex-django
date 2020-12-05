from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    contact = models.CharField(max_length=15)
    image_url = models.TextField(default="https://www.cmcaindia.org/wp-content/uploads/2015/11/default-profile-picture-gmail-2.png")

    #created at and updated at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
