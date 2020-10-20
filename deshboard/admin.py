from django.contrib import admin
from deshboard.models import Movie, Moviesgenre, Post
# Register your models here.


admin.site.register(Moviesgenre)
admin.site.register(Movie)
admin.site.register(Post)
