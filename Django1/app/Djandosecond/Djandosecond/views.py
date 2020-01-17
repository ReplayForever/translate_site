from django import *
from django.http import HttpResponse

def first_project(request):
   return HttpResponse ('<h1> Hellow </h2>')