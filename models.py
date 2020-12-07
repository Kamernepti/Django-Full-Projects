from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validation(self, postData):
        errors={}
        if len(postData["name"]) < 4:
            errors["name"]= "Course name must be at least 5 characters long"
        if len(postData["description"]) < 14:
            errors["name"]= "Course description must be at least 15 characters long"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=CourseManager()