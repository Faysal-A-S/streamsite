from django.contrib import admin

# Register your models here.
from .models import Movie,Genre,Type
admin.site.register(Movie)
admin.site.register(Type)
admin.site.register(Genre)