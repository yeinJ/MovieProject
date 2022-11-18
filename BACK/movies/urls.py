from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/recommended/', views.movie_recommend),
    
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/like/', views.movie_like),
    
    path('movies/<int:movie_pk>/reviews/', views.review_create),

    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/like/', views.review_like),
    
]