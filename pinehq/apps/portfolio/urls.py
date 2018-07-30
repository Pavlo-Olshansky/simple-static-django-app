from django.urls import re_path

from portfolio.views import PortfolioView


urlpatterns = [
    re_path(r'^$', PortfolioView.as_view(), name='index'),
]
