from django.db import models

# Create your models here.

class Courses(models.Model):
    name=models.TextField()
    img=models.FileField()
    