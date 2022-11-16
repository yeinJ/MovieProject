from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie
from .serializers.movies import MovieSerializer

# 전체 영화 목록 페이지 조회
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    # 단일 영화 페이지 조회
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

