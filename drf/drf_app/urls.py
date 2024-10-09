from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', IndexApi.as_view()),
    path('movie_list/', movieList, name='movie_list')
]

urlpatterns = format_suffix_patterns(urlpatterns)