# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    user = models.CharField(max_length=20)
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=100, blank=True, null=True)
    aboutme = models.TextField(db_column='aboutMe', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    active = models.CharField(max_length=11)
    role = models.IntegerField()
    profile = models.CharField(max_length=155)
    theme = models.CharField(max_length=33, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Allmovies(models.Model):
    movietitle = models.CharField(db_column='MovieTitle', max_length=255, blank=True, null=True,default='Values')  # Field name made lowercase.
    movieyear = models.TextField(db_column='MovieYear', blank=True, null=True,default=2020)  # Field name made lowercase. This field type is a guess.
    movieid = models.CharField(db_column='MovieID', unique=True, max_length=55, blank=True, null=True)  # Field name made lowercase.
    moviequality = models.CharField(db_column='MovieQuality', max_length=55,blank=True, default=720)  # Field name made lowercase.
    moviecategory = models.CharField(db_column='MovieCategory', max_length=55,blank=True)  # Field name made lowercase.
    movietrailer = models.CharField(db_column='MovieTrailer', max_length=500,blank=True )  # Field name made lowercase.
    movieratings = models.FloatField(db_column='MovieRatings', blank=True, null=True)  # Field name made lowercase.
    moviegenre = models.CharField(db_column='MovieGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    moviedate = models.DateField(db_column='MovieDate', blank=True, null=True)  # Field name made lowercase.
    movielang = models.CharField(db_column='Movielang', max_length=55, blank=True, null=True)  # Field name made lowercase.
      # Field name made lowercase.
    movieruntime = models.CharField(db_column='MovieRuntime', max_length=33, blank=True, null=True)  # Field name made lowercase.
    moviekeywords = models.TextField(db_column='MovieKeywords', blank=True, null=True)  # Field name made lowercase.
    moviestory = models.TextField(db_column='MovieStory', blank=True, null=True)  # Field name made lowercase.
    moviewatchlink = models.TextField(db_column='MovieWatchLink', blank=True, null=True)  # Field name made lowercase.
    moviesubtitle = models.TextField(db_column='MovieSubtitle', blank=True, null=True)  # Field name made lowercase.
    movieactors = models.TextField(db_column='MovieActors', blank=True, null=True)  # Field name made lowercase.
    moviesize = models.CharField(db_column='MovieSize', max_length=55, blank=True, null=True)  # Field name made lowercase.
    poster = models.ImageField( upload_to="", default='juggernaut.jpg')
    uploadeduser = models.CharField(db_column='uploadedUser', max_length=55, blank=True, null=True)  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='uploadTime',auto_now=True)  # Field name made lowercase.
    views = models.IntegerField(blank=True, null=True)
    published = models.IntegerField(default=0)
    moviehomepage = models.CharField(db_column='Moviehomepage', max_length=255)

    
    
    class Meta:
        managed = False
        db_table = 'allmovies'
    
    def __str__(self):
        if self.movietitle ==None:
            self.movietitle ='Values'
           

        return self.movietitle    
    

class DiskSetup(models.Model):
    path = models.CharField(db_column='Path', max_length=255)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disk_setup'


class Games(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=555)
    cover_pic = models.CharField(max_length=555)
    trailer = models.CharField(max_length=222)
    download = models.CharField(max_length=111)
    details = models.TextField()
    con_cat = models.CharField(max_length=55)
    hit = models.IntegerField()
    filesize = models.CharField(max_length=55)
    published = models.IntegerField()
    uploader = models.CharField(max_length=155)

    class Meta:
        managed = False
        db_table = 'games'


class Logininfo(models.Model):
    username = models.CharField(max_length=25)
    ipaddress = models.CharField(max_length=155)
    serverip = models.CharField(max_length=155)
    login = models.IntegerField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logininfo'


class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    parent = models.CharField(max_length=33)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu'


class Moviesgenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=33)

    class Meta:
        managed = False
        db_table = 'moviesgenre'
    def __str__(self):
        return self.name
        


class Notification(models.Model):
    user = models.CharField(max_length=33)
    noti = models.CharField(max_length=255)
    ndatetime = models.DateTimeField(db_column='nDatetime')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'


class Settings(models.Model):
    websitename = models.CharField(db_column='websiteName', max_length=255)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='websiteUrl', max_length=255)  # Field name made lowercase.
    webid = models.IntegerField(db_column='WebID')  # Field name made lowercase.
    websitelogo = models.CharField(db_column='websiteLogo', max_length=255)  # Field name made lowercase.
    theme = models.CharField(max_length=100)
    layout = models.CharField(max_length=55)
    skin = models.CharField(max_length=11)
    slider = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'settings'


class Shoutbox(models.Model):
    exordid = models.CharField(max_length=155)
    date = models.DateTimeField()
    text = models.TextField()
    reply_text = models.CharField(max_length=255)
    user_ip = models.CharField(max_length=115)
    cate = models.CharField(max_length=55)

    class Meta:
        managed = False
        db_table = 'shoutbox'


class Software(models.Model):
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    title = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)
    downlink = models.TextField(db_column='downLink')  # Field name made lowercase.
    cata = models.IntegerField()
    filesize = models.CharField(max_length=155)
    upby = models.CharField(max_length=155)
    publish = models.IntegerField()
    views = models.IntegerField()
    picu = models.IntegerField(db_column='picU')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software'


class Todaypageviews(models.Model):
    ipaddress = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    hit_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'todaypageviews'


class Tvepisodes(models.Model):
    tvid = models.IntegerField(db_column='TVID')  # Field name made lowercase.
    episode_number = models.IntegerField()
    season_number = models.IntegerField()
    epiid = models.IntegerField(db_column='EPIID', unique=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    still_path = models.CharField(max_length=555)
    overview = models.TextField()
    quality = models.CharField(max_length=55)
    watchlink = models.TextField()
    air_date = models.DateField()
    up_time = models.DateTimeField()
    hit = models.IntegerField()
    upby = models.CharField(max_length=255)
    published = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tvepisodes'


class Tvgenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=155)

    class Meta:
        managed = False
        db_table = 'tvgenre'
    def __str__(self):
        return self.name
    


class Tvseries(models.Model):
    tvtitle = models.CharField(db_column='TVtitle', max_length=255,default='Values')  # Field name made lowercase.
    tvid = models.IntegerField(db_column='TVID', unique=True)  # Field name made lowercase.
    tvcategory = models.CharField(db_column='TVcategory', max_length=55,blank=True)  # Field name made lowercase.
    tvtrailer = models.CharField(db_column='TVtrailer', max_length=255,blank=True)  # Field name made lowercase.
    tvratings = models.FloatField(db_column='TVRatings',blank=True)  # Field name made lowercase.
    tvgenre = models.CharField(db_column='TVgenre', max_length=255,blank=True)  # Field name made lowercase.
    tvrelease = models.IntegerField(db_column='TVrelease',blank=True)  # Field name made lowercase.
    tvlang = models.CharField(db_column='TVlang', max_length=155,blank=True)  # Field name made lowercase.
    
    tvruntime = models.CharField(db_column='TVruntime', max_length=55,blank=True)  # Field name made lowercase.
    tvkeywords = models.TextField(db_column='TVkeywords',blank=True)  # Field name made lowercase.
    tvstory = models.TextField(db_column='TVstory',blank=True)  # Field name made lowercase.
    tvactors = models.CharField(db_column='TVactors', max_length=255,blank=True)  # Field name made lowercase.
    tvposter = models.CharField(db_column='TVposter', max_length=255,blank=True)  # Field name made lowercase.
    uploadeduser = models.CharField(db_column='uploadedUser', max_length=55, blank=True)  # Field name made lowercase.
    uploadtime = models.DateTimeField(db_column='uploadTime',auto_now=True)  # Field name made lowercase.
    views = models.IntegerField()
    published = models.IntegerField()
    tvhomepage = models.CharField(db_column='TVhomepage', max_length=155)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tvseries'
    def __str__(self):
        return self.tvtitle
    