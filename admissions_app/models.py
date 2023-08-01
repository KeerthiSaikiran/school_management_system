from enum import auto

from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    father_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=100)
    admission_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name