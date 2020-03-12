from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterUserForm, ResetPasswordForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


class BaseView(View):
    def get(self, request):
        return TemplateResponse(request, 'index.html')



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return TemplateResponse(request, 'login.html', {'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("index")
            else:
                return TemplateResponse(request, 'login.html')
        return render(request, "login.html", context={"form": form, "username":form.username, "password":form.password})


def LogoutUser(request):
    logout(request)
    return redirect('index')

class ResetPasswordView(View):
    def get(self, request, pk):
        form = ResetPasswordForm()
        us = User.objects.get(id=pk)
        return render(request, 'reset-password.html', context={'form':form, 'us': us})
    def post(self, request, pk):
        form = ResetPasswordForm(request.POST)
        us = User.objects.get(id=pk)
        if form.is_valid():
            us.new_password = form.cleaned_data('new_password')
            us.new_password2 = form.cleaned_data('new_password2')
            if us.new_password == us.new_password2:
                us.set_password(request.POST.get('new_password'))
                us.save()
            else:
                HttpResponse('Hasła nie zgadzają się! Proszę wprowadzić ponownie')
            return HttpResponseRedirect('/profile/<int:pk>')



class RegisterView(View):
    def get(self, request):
        Registerform = RegisterUserForm()
        return TemplateResponse(request, 'register.html', {'Registerform':Registerform})
    def post(self, request):
        Registerform = RegisterUserForm(request.POST)
        error = []
        if Registerform.is_valid():
            first_name = Registerform.cleaned_data['first_name']
            last_name = Registerform.cleaned_data['last_name']
            username = Registerform.cleaned_data['username']
            password = Registerform.cleaned_data['password']
            password_again = Registerform.cleaned_data['password_again']
            email = Registerform.cleaned_data['email']
            if not User.objects.filter(username=username).exists():
                if password == password_again:
                    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
                    user.save()
                    return HttpResponseRedirect('index')
                else:
                    error.append('Hasła nie są jednakowe')
            else:
                error.append('Podany użytkownik już idtnieje')
        return render(request, 'index.html', context={'Registerform':Registerform})

