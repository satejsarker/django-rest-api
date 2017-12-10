from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Casino(models.Model):
    name=models.CharField(max_length=50)
    adress=models.CharField(max_length=200)
    created_at=models.DateField(auto_now_add=True)
    modified_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.name