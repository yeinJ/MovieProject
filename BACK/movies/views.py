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


def find_sim_movie(like_movie_ids, movie_ids, sorted_ind, top_n):
    recommend_movies_ids = []

    for id in like_movie_ids:
        # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서 코사인 유사도 순으로 top_n 개의 index 추출
        idx = movie_ids.index(id)
        similar_indexes = sorted_ind[idx, :(top_n)]
        similar_indexes = similar_indexes.reshape(-1).tolist()
        recommend_movies_ids += [movie_ids[x] for x in similar_indexes if (movie_ids[x] not in recommend_movies_ids)]

    return recommend_movies_ids


# # 추천 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_recommend(request):
    serializer = UserSerializer(request.user)
    like_movies_id = [movie['id'] for movie in serializer.data['like_movies']]
    print('like_movies: ', like_movies_id)

    # 유저가 찜한 영화 목록이 있는 경우
    if len(like_movies_id) > 0:
        # 1. 유저가 찜한 영화들의 장르 기반 코사인 유사도를 계산하여, 추천 영화 아이디 추출 (100개 정도)
        sim_path = 'movies/fixtures/sim_df.csv'

        sim_df = pd.read_csv(sim_path, encoding='utf-8')
        sim_df = sim_df.set_index('movie_id', drop=True)

        movie_ids = sim_df.index.tolist()

        sim_list = sim_df.values.tolist()
        sim_np = np.array(sim_list)
    
        genre_sorted_ind = sim_np.argsort()[:, ::-1]

        
        n = max(100 // len(like_movies_id), 1)
        recommend_movies_ids = find_sim_movie(like_movies_id, movie_ids, genre_sorted_ind, n)
        recommend_movies_ids = [id for id in recommend_movies_ids if id not in like_movies_id]

        # 2. 추천 영화 아이디를 가진 영화 객체 저장
        recommend_movies = []
        for id in recommend_movies_ids:
            try:
                movie = Movie.objects.get(id=id)
                recommend_movies.append(movie)
            except Exception as e:
                print(e)
                print(id)

        # 3. vote_average를 기준으로 내림차순 정렬하여 상위 35개 영화 정보 반환
        sorted_recommend_movies = sorted(recommend_movies, key=lambda movie: movie.vote_average, reverse=True)[:35]
        serializer = MovieSerializer(sorted_recommend_movies, many=True)
        return Response(serializer.data)

    
    else:
        return Response(False)


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