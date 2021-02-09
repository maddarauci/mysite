#blog/models.py
from django.db import models


from django.contrib.auth.models import User

# media urls stuff


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # the time needs to be more accurate
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# a model for handling images in the with the "media url" part
# exmaple model below 
'''
uploading images into django (hopefuly)
'''

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    # stores images in date archives like 2021/2/2
    #image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

