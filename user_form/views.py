from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from .forms import UserForm
from .models import Form, Skills
from django.http import HttpResponse, HttpResponseRedirect


class FirstPage(View):
    form_class = UserForm
    template_name = 'user_form/form.html'
    success_url = 'google.com'

    def get(self, request):
        form = self.form_class(None)
        user = request.user
        print(user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        form.save(self)

def load_skills(request):
    category_id = request.GET.get('category')
    skills = Skills.objects.filter(category_id = category_id).order_by('name')
    return render(request, 'user_form/skills.html', {'skills': skills})