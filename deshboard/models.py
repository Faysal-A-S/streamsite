from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
# Status
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Movie(models.Model):
    # Field name made lowercase.
    movietitle = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    movieyear = models.TextField(blank=True, null=True, default=2020)
    # Field name made lowercase.
    movieid = models.CharField(
        unique=True, max_length=55, blank=True, null=True)
    # Field name made lowercase.
    moviequality = models.CharField(
        max_length=55, blank=True, default=720)
    # Field name made lowercase.
    moviecategory = models.CharField(
        max_length=55, blank=True)
    # Field name made lowercase.
    movietrailer = models.CharField(
        max_length=500, blank=True)
    # Field name made lowercase.
    movieratings = models.FloatField(
        blank=True, null=True)
    # Field name made lowercase.
    moviegenre = models.CharField(
        max_length=255, blank=True, null=True)
    # Field name made lowercase.
    moviedate = models.DateField(blank=True, null=True)
    # Field name made lowercase.
    movielang = models.CharField(
        max_length=55, blank=True, null=True)
    # Field name made lowercase.
    moviehomepage = models.CharField(
        max_length=255, blank=True, null=True)
    # Field name made lowercase.
    movieruntime = models.CharField(
        max_length=33, blank=True, null=True)
    # Field name made lowercase.
    moviekeywords = models.TextField(
        blank=True, null=True)
    # Field name made lowercase.
    moviestory = models.TextField(
        blank=True, null=True)
    # Field name made lowercase.
    moviewatchlink = models.TextField(
        blank=True, null=True)
    # Field name made lowercase.
    moviesubtitle = models.TextField(
        blank=True, null=True)
    # Field name made lowercase.
    movieactors = models.TextField(
        blank=True, null=True)
    # Field name made lowercase.
    moviesize = models.CharField(
        max_length=55, blank=True, null=True)

    poster = models.ImageField(upload_to="", blank=True)
    # Field name made lowercase.
    uploadeduser = models.CharField(
        max_length=55, blank=True, null=True)
    # Field name made lowercase.
    uploadtime = models.DateTimeField()
    views = models.IntegerField(blank=True, null=True)
    published = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-uploadtime']

    def __str__(self):
        return self.movietitle


class Moviesgenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=33)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
