from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from accounts.serializers import UserSerializer

import pandas as pd
import numpy as np
import csv


def find_sim_movie(idx, sorted_ind, top_n=10):
    # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서 유사도 순으로 top_n 개의 index 추출
    similar_indexes = sorted_ind[idx, :(top_n)]
    
    #dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    similar_indexes = similar_indexes.reshape(-1)

    # index 반환
    return similar_indexes.tolist()


# 추천 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_recommend(request):
    simi_path = 'C:/Users/multicampus/Desktop/FINAL_PJT/PJT_GITHUB/BACK/movies/fixtures/sim_df2.csv'

    simi_df = pd.read_csv(simi_path, encoding='utf-8')
    simi_df = simi_df.set_index('movie_id', drop=True)

    simi_list = simi_df.values.tolist()
    simi_np = np.array(simi_list)
    simi_sorted_ind = simi_np.argsort()[:, ::-1]


    serializer = UserSerializer(request.user)
    print(serializer.data)
    like_movies_idx = [movie['id'] for movie in serializer.data['like_movies']]
    
    recommend_movie_idx = []
    for idx in like_movies_idx:
        recommend_movie_idx += find_sim_movie(idx, simi_sorted_ind)
    
    recommend_movie_idx = [idx for idx in recommend_movie_idx if idx not in like_movies_idx]
    recommend_movie_idx = set(recommend_movie_idx)
    recommend_movie_idx = sorted(recommend_movie_idx)

    
    print(like_movies_idx)
    print(recommend_movie_idx)
    
    return Response(True)


# 전체 영화 목록 조회
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


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
