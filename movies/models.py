from django.db import models

# Create your models here.
class Genre(models.Model):
    genrename = models.CharField( max_length=50)
    def __str__(self):
        return self.genrename

class Type(models.Model):
    typename = models.CharField( max_length=50)
    def __str__(self):
        return self.typename


class Movie(models.Model):
    title = models.CharField( max_length=50)
    description  =models.TextField(max_length =500)
    image = models.ImageField( upload_to="movie_img",blank = True)
    video  =  models.FileField( upload_to="movie_img", max_length=100)
    date  = models.DateField( auto_now=True)
    duration =  models.CharField( max_length=10)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    vtype = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    


    