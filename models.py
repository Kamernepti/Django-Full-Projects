from __future__ import unicode_literals
from django.db import models

#added for validation
class ShowManager(models.Manager):
    def basic_validation(self, postData):
        errors={}
        if len(postData['title']) < 1:
            errors['title']="Title needs at least 1 character"
        if len(postData['network'])<1:
            errors['network']= "Network Required"
        if len(postData['release_date']) < 2:
            errors['release_date'] = "Release Date Required"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField(auto_now=False)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects= ShowManager()   #added for validation
