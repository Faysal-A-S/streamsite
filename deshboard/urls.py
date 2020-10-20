from django.urls import path
from .import views
from deshboard.views import deshboard, add_movie,  show_all_movies,  add_moviesgenre, post_new, post_edit
from deshboard.views import delete_post, delete_movie, edit_movie
urlpatterns = [
    # For Movie
    path('', views.deshboard, name='deshboard'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('all_movies/', views.show_all_movies, name='all_movies'),
    path('edit_movie/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:pk>/', views.delete_movie, name='delete_movie'),
    # path('unpublishedmovies/', views.un_published_movie, name='unpublishedmovies'),

    # for Movie genre
    path('add_moviesgenre/', views.add_moviesgenre, name='add_moviesgenre'),

    # for test post
    path('post_new/', views.post_new, name='post_new'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),

]
