from django.shortcuts import render,HttpResponse
from .models  import Allmovies,Moviesgenre,Tvepisodes,Tvgenre,Tvseries
from  .test_imdb import webscrapper
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    context = {
        'movies':Allmovies.objects.filter().order_by('-id'),
         'lmovies':Allmovies.objects.filter().order_by('-id')[1:3],
         'fmovies':Allmovies.objects.filter().order_by('-id')[:1],
         'countmovies':Allmovies.objects.count(),
         'tvseries':Tvseries.objects.count(),
    }
      
    if Allmovies.objects.filter(movietitle ='Values'):
    
        movie =Allmovies.objects.get(movietitle='Values')
        link = movie.moviehomepage
        a = webscrapper(link)
        print('hello world')
        genres = a['genre']
        moviegenre =', '.join(genres)
        sentence = a['stars']
        moviestar =", ".join(sentence)
            # print(a['video_length'])
        movietitle = a['title']
        moviedescription = a['description']
        # moviedate = a['release_date']
        movieruntime = a['video_length']
        saverecord = movie
        saverecord.movietitle = movietitle
        saverecord.moviegenre = moviegenre
        saverecord.movieactors=moviestar
        saverecord.moviestory =moviedescription
        # saverecord.moviedate = moviedate
        saverecord.movieruntime = movieruntime
        saverecord.save()
    
    # context = {
    #     'movies':Movie.objects.filter().order_by('-id'),
    #     'lmovies':Movie.objects.filter().order_by('-id')[1:3],
    #      'fmovies':Movie.objects.filter().order_by('-id')[:1],
    #     'Genre':Genre.objects.all(),
    #     'Type':Type.objects.all()
    # }
    return render(request,'movies/home.html',context)




def video(request,id):
    movie  = Allmovies.objects.get(pk = id)
    # tvseries  = Tvseries.objects.get(pk = id)
    
  
    star  = movie.movieactors[:-1]
    content = {
        'movie':movie,
        'title':movie.movietitle,
        'description':movie.moviestory,
        'release_date':movie.movieyear,
        'moviecatagory':movie.moviecategory,
        'movierating':movie.movieratings,
        'stars':star,
        'moviegenre':movie.moviegenre
    }
    return render(request,'movies/video.html',content)

def search(request,id):
    movies = Allmovies.objects.filter(moviecategory= id).order_by('-id')
    # types = Type.objects.get(pk = id)     
    context = {
        'movies':movies,
        # 'types' :types
        
    }
    return  render(request,'movies/search.html',context)    



def searches(request,search):

     tvseries = Tvseries.objects.filter(tvtitle__icontains=search)
     movies = Allmovies.objects.filter(movietitle__icontains=search) 
     
     context = {
         'movies':movies,
         'tvseries':tvseries
     } 
     return render(request,'movies/searches.html',context) 
  
def movieupdate(request,id=None):
    if request.method=="POST":
        movie =Allmovies.objects.get(pk=id)
        link = movie.moviehomepage
        a = webscrapper(link)
        print('hello world')
        genres = a['genre']
        moviegenre =', '.join(genres)
        sentence = a['stars']
        moviestar =", ".join(sentence)
        # print(a['video_length'])
        movietitle = a['title']
        moviedescription = a['description']
        moviedate = a['release_date']
        movieruntime = a['video_length']
        saverecord = Allmovies()
        saverecord.movietitle = movietitle
        saverecord.moviegenre = moviegenre
        saverecord.movieactors=moviestar
        saverecord.moviestory =moviedescription
        saverecord.moviedate = moviedate
        saverecord.movieruntime = movieruntime
        saverecord.save()
    return HttpResponseRedirect('/')