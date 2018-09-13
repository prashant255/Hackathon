from django.db import models
from django.contrib.auth.models import User

"""CATEGORY_CHOICES = (
    ('accounting', 'accounting'),
    ('agriculture', 'agriculture'),
    ('air-hostess','air-hostess'),
    ('animation','animation'),
    ('architecture','architecture'),
    ('automobile','automobile'),
    ('call-center','call-center'),
    ('clerk','clerk'),
    ('computer-operator','computer-operator'),
    ('data-entry','data-entry'),
    ('defence','defence'),
    ('documentation','documentation'),
    ('editing','editing'),
    ('engineering','engineering'),
    ('excel','excel'),
    ('finance','finance'),
    ('flex','flex'),
    ('insurance','insurance'),
    ('lecturer','lecturer'),
    ('librarian','librarian'),
    ('manual-testing','manual-testing'),
    ('marketing','marketing'),
    ('media','media'),
    ('multimedia','multimedia'),
    ('nursing','nursing'),
    ('pharmacist','pharmacist'),
    ('photoshop', 'photoshop'),
    ('railway', 'railway'),
    ('retail', 'retail'),
    ('teaching','teaching'),
    ('telecom','telecom'),
    ('video-editing','video-editing'),
    ('web-designing','web-designing'),
)"""
class Category(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill

class Form(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    income = models.BigIntegerField(default=0)
    edu_qualification = models.CharField(max_length=100)
    desired_skills = models.CharField(max_length=50)
    job = models.CharField(max_length=100)