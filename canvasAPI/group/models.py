from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=300)
    ##  agregar campo de course