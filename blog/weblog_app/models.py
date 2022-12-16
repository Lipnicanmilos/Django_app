from contextlib import nullcontext
from datetime import date
# from pyexpat import model
from django.db import models
# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
now = timezone.now()

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey

# Create your models here.
from django.contrib.auth.models import User

#  import ChainedManyToManyField


# class User(AbstractUser):
#         image = models.ImageField(upload_to='images/')

from django.core.exceptions import ValidationError

def validate_image(image):
    file_size = image.file.size
    limit = 2621440
    if file_size > limit:
        raise ValidationError("Max size of file is %s KB" % limit)

    # 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB - 104857600
# 250MB - 214958080
# 500MB - 429916160

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(null=True, blank=True,)
    profile_image = models.ImageField(upload_to='managers/', default='managers/default.png', validators=[validate_image], help_text=("Please use our recommended dimensions: 1140 x 425 PX, 250 KB MAX"))

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Manager.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.manager.save()    
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    # body = RichTextField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
         
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #ak zmazem post tak aj komentar
    body = models.TextField()
    date = models.DateTimeField('date commented', auto_now_add=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}, {self.post.title}'

# # # # # # post end # # # # # #

class Season_name(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)

    @staticmethod
    def get_all_categories():
        return Season_name.objects.all()

    def __str__(self):
        return self.name

class Team(models.Model):
    season_name = models.ForeignKey(Season_name, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    # manager = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='teams/', default='teams/default.png')
    name = models.CharField(max_length=50)
    N_Matches = models.IntegerField(default=0)
    N_Wins = models.IntegerField(default=0)
    N_Draws = models.IntegerField(default=0)
    N_Losses = models.IntegerField(default=0)
    Score_P = models.IntegerField(default=0)
    Score_M = models.IntegerField(default=0)
    Score_result = models.IntegerField(default=0)
    Points = models.IntegerField(default=0)

    @staticmethod
    def get_all_teams():
        return Team.objects.all()
    
    # @property
    # def Score(Team):
    #     Score = Team.Score_P - Team.Score_M
    #     return Score
    # def save(self, *args, **kwargs):
    #     self.Score= self.Score_P - self.Score_M
    #     super(Team, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.season_name} / {self.manager} / {self.name}"


class Match(models.Model):
    season_name = models.ForeignKey(Season_name, on_delete=models.CASCADE)
    Team_home = models.ForeignKey(Team, related_name='home' ,on_delete=models.CASCADE)
    Team_visitor = models.ForeignKey(Team, related_name='visitor',on_delete=models.CASCADE)
    Team_home_goal = models.IntegerField(default=0)
    Team_visitor_goal = models.IntegerField(default=0)
    date = models.DateTimeField() 
    body = models.TextField(blank=True)

    # def init(self, db_field):
    #     kwargs = super(Match, self).get_form_kwargs()
    #     kwargs['Team_home'] = self.self.season_name

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     # Only show people managed by the current user
    #     return qs.filter(Team_home__season_name__id=self.season_name.id)

# class Match(models.Model):
#     season_name = models.ForeignKey(Season_name, on_delete=models.CASCADE)
#     # Team_home = models.ForeignKey(Team, related_name='home' ,on_delete=models.CASCADE)
#     Team_home = ChainedForeignKey(
#         Team,
#         chained_field="season_name",
#         chained_model_field="season_name",
#         show_all=False,
#         auto_choose=True,
#         sort=True)  
#     Team_visitor = models.ForeignKey(Team, related_name='visitor',on_delete=models.CASCADE)
#     Team_home_goal = models.IntegerField(default=0)
#     Team_visitor_goal = models.IntegerField(default=0)
#     date = models.DateTimeField() 
#     body = models.TextField(blank=True)

    def save(self):
        # team_home_points = self.Team_home.Points
        # print(self.Team_home.id)
        # print(type(team_home_points))
        # team_visitor_points = self.Team_visitor.Points
        # team_points = Team.objects.filter(Points=self.Team_home.Points).first()
        # print(team_points.Points)
        obj0 = self.Team_home
        obj0.N_Matches += 1
        obj0.save()
        obj12 = self.Team_home
        obj12.Score_P += self.Team_home_goal
        obj12.save()
        obj13 = self.Team_home
        obj13.Score_M += self.Team_visitor_goal
        obj13.save()
        obj14 = self.Team_visitor
        obj14.Score_P += self.Team_visitor_goal
        obj14.save()
        obj15 = self.Team_visitor
        obj15.Score_M += self.Team_home_goal
        obj15.save()  
        obj1 = self.Team_visitor
        obj1.N_Matches += 1
        obj1.save()

        obj16 = self.Team_visitor
        obj16.Score_result -= self.Team_home_goal
        obj16.Score_result += self.Team_visitor_goal
        obj16.save() 

        obj17 = self.Team_home
        obj17.Score_result += self.Team_home_goal
        obj17.Score_result -= self.Team_visitor_goal
        obj17.save() 

        super().save()
        if self.Team_home_goal > self.Team_visitor_goal:
            obj2 = self.Team_home
            obj2.Points += 3
            obj2.save()
            obj6 = self.Team_home
            obj6.N_Wins += 1
            obj6.save()
            obj10 = self.Team_visitor
            obj10.N_Losses += 1
            obj10.save()
            super().save() 
        elif self.Team_home_goal < self.Team_visitor_goal:
            obj3 = self.Team_visitor
            obj3.Points += 3
            obj3.save()
            obj7 = self.Team_visitor
            obj7.N_Wins += 1
            obj7.save()
            obj11 = self.Team_home
            obj11.N_Losses += 1
            obj11.save()
            super().save()
        else:
            obj4 = self.Team_home
            obj4.Points += 1
            obj4.save() 
            obj5 = self.Team_visitor
            obj5.Points += 1
            obj5.save()
            obj8 = self.Team_home
            obj8.N_Draws += 1
            obj8.save()
            obj9 = self.Team_visitor
            obj9.N_Draws += 1
            obj9.save()
            super().save()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     print(type(self.Team_home.Points))
    #     self.Team_home.Points += int(3)
    #     print(self.Team_home.Points)
    #     print(dir(self.Team_home.Points))
    #     print(type(self.Team_home.Points))
    #     # self.Team_home.Points.update(answer_views=F('answer_views') + 1)
    #     self.Team_home.Points.update()
    #     bill_detail.save(update_fields = ['last_price'])