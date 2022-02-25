from re import template
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages_templates/home.html"

class AboutPageView(TemplateView):
    template_name = "pages_templates/about.html"

## from django.shortcuts import render