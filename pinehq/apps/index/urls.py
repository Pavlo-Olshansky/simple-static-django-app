from django.urls import re_path

from index.views import IndexView


urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
]
