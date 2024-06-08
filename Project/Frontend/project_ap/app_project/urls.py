from django.urls import path
from . import views

urlpatterns = [
    path('genre/<str:genre_name>/songs/', views.get_genre_songs),
    path('playlist/<str:playlist_name>/add-song/<str:song_title>/', views.add_song_to_playlist),
    path('playlist/<str:playlist_name>/remove-song/<str:song_title>/', views.remove_song_from_playlist),
    path('playlist/<str:playlist_name>/songs/', views.get_playlist_songs),
    path('register/', views.register),
    path('login/', views.login),
    path('search/', views.search),
    path('create-playlist/', views.create_playlist),
    path('add-song-to-playlist/', views.add_song_to_a_playlist),
    path('upload-song/', views.upload_song),
]
