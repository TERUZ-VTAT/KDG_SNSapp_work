from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Chat(TemplateView):
    template_name = 'chat.html'