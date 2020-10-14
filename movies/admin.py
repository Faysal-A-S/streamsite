from django.contrib import admin
from django.contrib.auth.models  import Group
# Register your models here.
from .models import Allmovies,Moviesgenre,Tvepisodes,Tvgenre,Tvseries

    


admin.site.site_header = "SolutionTent Dashboard"

admin.site.register(Allmovies)
admin.site.register(Moviesgenre)
admin.site.register(Tvepisodes)
admin.site.register(Tvgenre)
admin.site.register(Tvseries)
admin.site.unregister(Group)
