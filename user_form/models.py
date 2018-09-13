from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Form(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    income = models.BigIntegerField(default=0)
    edu_qualification = models.CharField(max_length=100)
    desired_skills = models.CharField(max_length=50)
    job = models.CharField(max_length=100)