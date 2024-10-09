from rest_framework import serializers


from django.contrib.auth.models import User
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['genre', 'release_year', 'min_rating', 'director']