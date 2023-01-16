from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TEAMLEADER = 'TEAMLEADER', 'TeamLeader'
        CLOSER = 'CLOSER', 'Closer'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'
        AGENT = 'AGENT', 'Agent'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class Student(User):
    base_role = User.Role.STUDENT

    class Meta:
        proxy = True


class Teacher(User):
    base_role = User.Role.TEACHER

    class Meta:
        proxy = True


class Agent(User):
    base_role = User.Role.AGENT

    class Meta:
        proxy = True


class Closer(User):
    base_role = User.Role.CLOSER

    class Meta:
        proxy = True


class TeamLeader(User):
    base_role = User.Role.TEAMLEADER

    class Meta:
        proxy = True
