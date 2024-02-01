from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.


class Welcome(TemplateView):
    template_name = 'test.html'


def firstPage(request):
    return redirect('chat/')
