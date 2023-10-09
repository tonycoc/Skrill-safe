from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Home(TemplateView):

    template_name = "home.html"

class view_404(TemplateView):
    template_name = "404.html"