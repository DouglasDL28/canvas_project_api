from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=300)
    user = models.OneToOneField(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Professor: {}'.format(self.name)