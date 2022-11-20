from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass



class Lead(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255, blank=True, null=True)
    age =  models.IntegerField(default=0, blank=True, null=True)
    agent =  models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Agent(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email




