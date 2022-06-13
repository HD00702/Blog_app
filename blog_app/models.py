from django.db import models
from django.utils import timezone
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content =models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_liked=models.BooleanField(default=False)

    def create(self): #save the post
        self.save()


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk}) #get the absolute url of a post

    def __str__(self):
        return self.title





