from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.conf.urls.static import static

# Create your views here.
class SingleOferta ():
    oferta = tutaj kod
    return render(request, 'single-oferta.html', {"oferta": oferta})

class MiastoOferty ():