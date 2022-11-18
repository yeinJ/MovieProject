from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# 전체 영화 목록 조회
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 추천 영화 목록 조회
@api_view(['GET'])
def movie_recommend(request):
    pass


# 단일 영화 detail 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 리뷰 등록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    # 리뷰 디테일 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 리뷰 수정
    elif request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(False)

    # 리뷰 삭제
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(False)


# 영화 좋아요 추가 / 삭제
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.movie_like_users.filter(pk=user.pk).exists():
        movie.movie_like_users.remove(user)
        liked = False
    else:
        movie.movie_like_users.add(user)
        liked = True
    
    return Response(liked)


# 리뷰 좋아요 추가 / 삭제
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.review_like_users.filter(pk=user.pk).exists():
        review.review_like_users.remove(user)
        liked = False
    else:
        review.review_like_users.add(user)
        liked = True
    
    return Response(liked)
