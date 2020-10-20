from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from movies.models import Allmovies,Moviesgenre,Tvepisodes,Tvgenre,Tvseries
from deshboard.forms import MoviesgenreForm, PostForm, MovieForm
from django.contrib import auth

# Create your views here.


def deshboard(request):
    count_movie = Allmovies.objects.all().count()
    count_unpublished_movie = Allmovies.objects.all().count()
    count_games = 0
    count_unpublished_games = 0
    count_tv_series = 0
    count_unpublished_tv_series = 0
    count_software = 0
    count_unpublished_software = 0
    context = {
        'count_movie': count_movie,
        'count_unpublished_movie': count_unpublished_movie,
        'count_games': count_games,
        'count_unpublished_games': count_unpublished_games,
        'count_tv_series': count_tv_series,
        'count_unpublished_tv_series': count_unpublished_tv_series,
        'count_software': count_software,
        'count_unpublished_software': count_unpublished_software
    }
    return render(request, 'deshboard/base.html', context)


# Create Operation for Movie:
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'deshboard/admin/add_movie.html', {'form': form})


# Read Operation for Movie:
def show_all_movies(request):
    count_movie = Allmovies.objects.all().count()
    movie_list = Allmovies.objects.all()
    context = {
        'movie_list': movie_list,
        'count_movie': count_movie
    }
    return render(request, 'deshboard/admin/all_movies.html', context)


# Update Operation for Movie:
def edit_movie(request, pk):
    movie = get_object_or_404(Allmovies, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.author = request.user
            movie.save()
            return redirect('all_movies')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'deshboard/admin/edit_movie.html', {'form': form})


# Delete Operation for Movie:
def delete_movie(request, pk):

    obj = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'obj': obj
    }
    return render(request, "deshboard/admin/delete_movie.html", context)


# For Unpublished Movie
# def un_published_movie(request):
#     count_unpublished_movie = Allmovies.objects.filter(published=0).count()
#     unpublished_movie = Allmovies.objects.filter(published=0)
#     context = {
#         'unpublished_movie': unpublished_movie,
#         'count_unpublished_movie': count_unpublished_movie
#     }
#     return render(request, 'deshboard/admin/unpublished_movie.html', context)


# Create Operation for Movie Genre:
def add_moviesgenre(request):
    if request.method == "POST":
        form = MoviesgenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = MoviesgenreForm()

    return render(request, 'deshboard/admin/add_moviesgenre.html', {'form': form})


# Create Operation
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'deshboard/admin/add_post.html', {'form': form})


# Update operation
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'deshboard/admin/post_edit.html', {'form': form})


# Delete operation:
def delete_post(request, pk):
    context = {}
    obj = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    return render(request, "deshboard/admin/delete_post.html", context)

def login(request):
    if request.method =='POST':
        username3 = request.POST['signinuser']
        password2 = request.POST['signinpass']
        
        user = auth.authenticate(username=username3,password=password2)
        if user is None:
            return  render(request,'deshboard/admin/login.html',{'lerror':'Incorrect username or password'})

        else:
            auth.login(request,user)
            return redirect('deshboard')
                 
    elif request.method =='GET':
        return  render(request,'deshboard/admin/login.html')
    

def register(request):
    if request.method =='POST':
        username = request.POST['signupuser']
        password = request.POST['signuppass']
        cpassword =request.POST['confirmsignuppass']
        print(username,password)
        if  password == cpassword:
            try:
                user = User.objects.get(username=username)
                return  render(request,'deshboard/admin/register.html',{'error':'Username already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                auth.login(request,user)
                return redirect('deshboard')

        else:
            return  render(request,'deshboard/admin/register.html',{'rerror':'Password doesn\'t match'})
    elif request.method =='GET':
        return  render(request,'deshboard/admin/register.html')
    
def logout(request):
    auth.logout(request)
    return render(request,'deshboard/base.html')    