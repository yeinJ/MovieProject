from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from .models import Movie

# 전체 영화 목록 페이지 조회
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        context= {
            'movies': movies,
        }
        return render(request, 'movies/index.html', context)
