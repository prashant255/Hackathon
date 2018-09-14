from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from user_form.models import Form


class SignUp(View):
    form_class = UserForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    a=Form()
                    a.user = user
                    a.save()
                    return render(request, 'user_form/form_form.html', {'form': form})
        return render(request, self.template_name, {'form': form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            # log in user
            # return render(request, 'accounts/new.html')
            return redirect('http://127.0.0.1:8000/form/')
    else:
        form = AuthenticationForm()
    return render(request, 'loginpage.html', {'form': form})