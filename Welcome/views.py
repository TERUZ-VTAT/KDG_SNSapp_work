from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class Welcome(TemplateView):
    template_name = "test.html"