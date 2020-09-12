from django.shortcuts import render,redirect
from .models  import Movie,Genre,Type
# Create your views here.
def home(request):

    context = {
        'movies':Movie.objects.filter().order_by('-id'),
        'lmovies':Movie.objects.filter().order_by('-id')[1:3],
         'fmovies':Movie.objects.filter().order_by('-id')[:1],
        'Genre':Genre.objects.all(),
        'Type':Type.objects.all()
    }
    return render(request,'movies/home.html',context)




def video(request,id):
    movie  = Movie.objects.get(pk = id)
    context = {
        'movie':movie
    }
    return render(request,'movies/video.html',context)

def search(request,id):
    movies = Movie.objects.filter(vtype= id)
    types = Type.objects.get(pk = id)     
    context = {
        'movies':movies,
        'types' :types
        
    }
    return  render(request,'movies/search.html',context)    



def searches(request,search):

    
     movies = Movie.objects.filter(title__contains=search) 
     context = {
         'movies':movies
     } 
     return render(request,'movies/searches.html',context) 
  
            