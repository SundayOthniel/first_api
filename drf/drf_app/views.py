from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import MovieSerializer
from .models import Movies
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse


@api_view(['GET'])
def movieList(request, format=None):
    if request.method == 'GET':
        genre = request.query_params.get('genre')
        release_year = request.query_params.get('release_year')
        min_rating = request.query_params.get('min_rating')
        director = request.query_params.get('director')
        
        movies = Movies.objects.all()

        if genre:
            movies = movies.filter(genre__iexact=genre)
        if release_year:
            movies = movies.filter(release_year__iexact=release_year)
        if min_rating:
            movies = movies.filter(min_rating__iexact=min_rating)
        if director:
            movies = movies.filter(director__iexact=director)
        serialize_movies = MovieSerializer(movies, many=True)
        if not serialize_movies.data:
            return Response('Match not found...')
        return Response(serialize_movies.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class IndexApi(APIView):
    def get(self, request, format=None):
        return Response(
            {'movies': reverse('movie_list', request=request, format=format)}
        )