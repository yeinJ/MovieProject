from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', )

class ReviewSerializer(serializers.ModelSerializer):
    review_like_users = UserSerializer(many=True, read_only=True)
    review_like_users_count = serializers.IntegerField(source='review_like_users.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    movie_like_users = UserSerializer(many=True, read_only=True)
    movie_like_users_count = serializers.IntegerField(source='movie_like_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
