from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review

class UserSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title', 'content')
    
    like_movies = MovieSerializer(many=True, read_only=True)
    like_reviews = ReviewSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'