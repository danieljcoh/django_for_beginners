from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"