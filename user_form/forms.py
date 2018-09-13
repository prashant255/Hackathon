from .models import Form
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = [ 'category', 'skills', 'income', 'edu_qualification', 'desired_skills', 'job',]