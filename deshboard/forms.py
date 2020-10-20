from django import forms
from deshboard.models import Movie, Moviesgenre, Post


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class TimeInput(forms.TextInput):
    input_type = 'time'


class PostForm(forms.ModelForm):

    class Meta(object):
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Post Title",
                    'required': 'true'

                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Post",
                    'required': 'true'
                }
            ),
        }


class MovieForm(forms.ModelForm):
    # form for movie
    class Meta:
        model = Movie
        fields = [
            'movietitle',
            'movieyear',
            'movieid',
            'moviequality',
            'moviecategory',
            'movietrailer',
            'movieratings',
            'moviegenre',
            'moviedate',
            'movielang',
            'moviehomepage',
            'movieruntime',
            'moviewatchlink',
            'moviesize',
            'uploadeduser',
            'uploadtime',
            'views',
            'moviekeywords',
            'moviestory',
            'moviesubtitle',
            'movieactors',
            'poster',
            'published'
        ]
        widgets = {
            'movietitle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Title",
                    'required': 'true'
                }
            ),
            'movieyear': forms.TextInput(
                attrs={
                    'class': ' form-control',
                    'placeholder': "Movie Year",
                }
            ),
            'movieid': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie ID",
                    'required': 'true'
                }
            ),
            'moviequality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Quality",
                    'required': 'true'
                }
            ),
            'moviecategory': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Category",
                    'required': 'true'
                }
            ),
            'movietrailer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Trailer",
                }
            ),
            'movieratings': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Ratings",
                }
            ),
            'moviegenre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Genre",
                    'required': 'true'
                }
            ),
            'moviedate': DateInput(),
            'movielang': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Movie Language",
                    'required': 'true'
                }
            ),
            'moviehomepage': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Home Page",
                }
            ),
            'movieruntime': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie RunTime",
                }
            ),
            'moviekeywords': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie KeyWords",
                }
            ),
            'moviestory': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Story",
                }
            ),
            'moviewatchlink': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Watch Link",
                    'required': 'true'
                }
            ),
            'moviesubtitle': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Subtitle",
                }
            ),
            'movieactors': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Actors",
                }
            ),
            'moviesize': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Size",
                }
            ),
            'poster': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'uploadeduser': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Upload User",
                }
            ),
            'uploadtime': DateTimeInput(),
            'views': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Movie Views ",
                }
            ),
            'published': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding-top: 1px;'
                }
            ),
        }


class MoviesgenreForm(forms.ModelForm):
    class Meta(object):
        model = Moviesgenre
        fields = ('id', 'name')
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Movie Genre ID",
                    'required': 'true'

                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Movie Genre Name",
                    'required': 'true'
                }
            ),
        }

    '''
    id = forms.IntegerField()
    name = forms.CharField(max_length=33)

    def clean(self):
        cleaned_data = super(MoviesgenreForm, self).clean()
        id = cleaned_data.get('id')
        name = cleaned_data.get('name')
        if not id and not name:
            raise forms.ValidationError('You have to write something!')
    '''
