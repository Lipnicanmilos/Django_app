# from multiprocessing.dummy import Manager
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment, Manager, Team, Match, Season_name


class PostCreateForm(forms.ModelForm):
    class Meta:
         model = Post
         fields = ("title","body")
         exclude = ["author"]

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'author']

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		# user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

from django.forms.utils import ErrorList

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = [
            'info',
            'profile_image'
        ]

            # 2.5MB - 2621440
            # 5MB - 5242880
            # 10MB - 10485760
            # 20MB - 20971520
            # 50MB - 5242880
            # 100MB - 104857600
            # 250MB - 214958080
            # 500MB - 429916160


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'season_name',
            'name',    
        ]
        # exclude = ['manager']

class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name","image","id")


# class MyCustomForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = "__all__"


class Match_form(forms.ModelForm):
    # season_name = forms.ModelChoiceField(queryset=Season_name.objects.all())
    season_name = Season_name.objects.all()
    
    def __init__(self, *args, **kwargs):
        super(Match_form, self).__init__(*args, **kwargs)

        seasons = [('', '---------')] + [(season_name.id, season_name.name) for season_name in Season_name.objects.all()]
        self.fields['season_name'].widget = forms.Select(
            choices = seasons,
            attrs={
                'id': 'id_season_name',
                'style': 'width:258px;',
                'onchange': 'getCities(this.value)'
            }
        )
      
