from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
'''
In a blog application database we have :
-> Image of the blog
-> Title of the Blog
-> Content of the Blog
-> Dates related to content creation and updation
-> Owner of the Blog
'''

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='blog')#-> use AWS
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    #this will handle the situation when the user deletes the featured_image from their profile
    '''This lines of code is extremely important to extract the uploaded images by the users from the AWS S3 buckets'''
    @property
    def imageURL(self):
        try:
            url = self.image.url #image url
        except:
            pass
        return url
    '''--------------------------------------------------------------------------------------------------------------------'''

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
