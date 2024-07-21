from django.db import models

# Create your models here.

class Info(models.Model):
        
      image = models.ImageField(upload_to='post_images/', blank=True, null=True)
      name = models.CharField(max_length=200)
      age=models.IntegerField((""))
      skills=models.CharField(max_length=200)
      city = models.TextField(default='Tehran')
      about=models.TextField()
      email=models.EmailField(blank=True,null=True)


      def __str__(self):

        return self.name
      