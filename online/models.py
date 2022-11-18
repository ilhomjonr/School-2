from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    last_name = models.CharField(max_length=255, default='None', null=True, blank=True)
    first_name = models.CharField(max_length=255, default='None', null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, default='2000-01-31')
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Lessons(models.Model):
    name = models.CharField(max_length=100)
    mini_desc = models.TextField(max_length=200, null=True, blank=True)
    desc = models.TextField(max_length=1000)
    img = models.ImageField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    teacher = models.CharField(max_length=100)
    video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    mini_desc = models.TextField(max_length=200, null=True, blank=True)
    desc = models.TextField(max_length=1000)
    img = models.ImageField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    teacher = models.CharField(max_length=100)
    video = models.FileField(null=True, blank=True)

    # lesson = models.ForeignKey(Lessons, related_name='lessons', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


