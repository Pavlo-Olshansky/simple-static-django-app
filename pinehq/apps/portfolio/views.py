from django.shortcuts import render
from django.views.generic.base import TemplateView


class PortfolioView(TemplateView):
    template_name = 'portfolio-masonary-2-column-no-gutter.html'
