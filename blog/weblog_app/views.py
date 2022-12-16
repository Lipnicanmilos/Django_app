from cgitb import html
from dataclasses import fields
from multiprocessing import context, managers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment, Manager, User, Team, Season_name, Match
from .forms import PostCreateForm, CommentForm, NewUserForm, UserForm, ProfileForm, TeamForm, TeamUpdateForm, PostUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import JsonResponse

# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.hashers import make_password

from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages


# from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage

from django.core.exceptions import ValidationError

# # # ## # # ## # # ## # # ## # # ## # # # logger # # # ## # # ## # # ## # #  
# Import the logging module
import logging

# Define the logging configurations
logging.config.dictConfig({
   # Define the logging version
    'version': 1,
    # Enable the existing loggers
    'disable_existing_loggers': False,
   
   # Define the formatters
    'formatters': {
        'console': {
            'format': '%(message)s'
        },
        'file': {
            'format': '%(message)s'
        },
   
   # Define the handlers
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'djangoapp.log'
        }
    },
   
   # Define the loggers
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],

        }
    }
}

})

# Create the loggers object
logger = logging.getLogger('__name__')

# # # # ## # # ## # # ## # # # end logger # # # ## # # ## # # ## # # ## # # ## # # #

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-id')

	# Paginator
	p = Paginator(posts, 3) 
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)
	
	usersview = Manager.objects.all() #navbar select
	context ={'posts': page, 'users':usersview}
	# zabezpecenie priradenie managera pri prihlaseni
	if request.user.is_authenticated: 
		context['manager'] = request.user
	
	return render(request, 'weblog_app/index.html', context)

# def base(request):
# 	users = Manager.objects.all()
# 	return render(request, 'weblog_app/base.html', {'users':users})

def post(request, post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('date')

    comment_form = CommentForm()
    usersview = Manager.objects.all() #navbar select

    return render(request, 'weblog_app/post.html', {'post': post, 'comments':comments, 'comment_form': comment_form, 'users':usersview})

class PostCreate(CreateView):
	model = Post
	template_name = "weblog_app/new_post.html"    
	form_class = PostCreateForm
	
	# def form_valid(self, form):
	# 	form.instance.author = self.request.user
	# 	self.object=form.save()
    # 	return super().form_valid(form)

	def form_valid(self, form):
		candidate = form.save(commit=False)
		candidate.author = User.objects.get(username=self.request.user)  # use your own profile here
		# print(candidate.author)
		candidate.save()
		return HttpResponseRedirect(reverse('index'))

class PostUpdate(UpdateView):
		model = Post
		template_name = "weblog_app/post_update_form.html"
		form_class = PostUpdateForm
		success_url = reverse_lazy('index')

class PostDelete(DeleteView):
    model = Post 
    template_name = "weblog_app/delete_post.html"
    success_url = reverse_lazy('index')

def addcomment(request, post_id):
	user = request.user
	post = get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
		# print(user)
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment_body = comment_form.cleaned_data['body']
			comment = Comment(post=post, body=comment_body, author=user)

			comment.save()

			return redirect('post', post_id=post.id)

def search(request):
    return render(request, 'weblog_app/base.html', {})

# livesearch # # # # # # # 
def livesearch(request, word, sid1, sid2):
    posts = Post.objects.filter(title__icontains=word)
    teams = Team.objects.filter(name__icontains=word)
    # managers = Manager.objects.filter(username__icontains=word)

    if len(teams) > 0 or len(posts) > 0:
        response = ''
        for p in teams:
             response += '<a href="' + reverse('team', args=(p.id,)) + f'">{p.name}</a><br/>'
        for p in posts:
             response += '<a href="' + reverse('post', args=(p.id,)) + f'">{p.title}</a><br/>'
			
    # elif len(posts) > 0:
    #     response = ''
    #     for p in posts:
    #          response += '<a href="' + reverse('post', args=(p.id,)) + f'">{p.title}</a><br/>'
    else:
        response = 'no seuggestion'
    return HttpResponse(response)

# # # # # USER # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register_request(request):
	usersview = Manager.objects.all() #navbar select

	user = request.user
	if user.is_authenticated:
		messages.info(request, f"You are now logged in as {str(user.username)}.") 
		return redirect("index")
	if request.method == "POST":
		form = NewUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, form.errors, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form, 'users':usersview})

def login_request(request):
	usersview = Manager.objects.all() #navbar select

	user = request.user
	if user.is_authenticated:
		messages.info(request, f"You are now logged in as {str(user.username)}.") 
		return redirect("index")
		# return HttpResponse("You are already authenticated as " + str(user.email))
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="account/login.html", context={"login_form":form, 'users':usersview})

def logout_view(request):
	
	if logout(request):
		messages.error(request,"Invalid username or password.")
			
	return redirect("index")

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'You are successfully logged out.')

@login_required(login_url='login')
def userprofile(request):
	usersview = Manager.objects.all() #navbar select

	# user = User.objects.get(id=user_id)
	user = request.user
	manager = Manager.objects.get(user=user)

	# user = request.user
	manager = request.user.manager

	p_form = ProfileForm(instance=manager)

	u_form = UserForm(instance=user)

	teams = Team.objects.filter(manager_id=manager.id) #select teams


	if request.method == 'POST':
		p_form = ProfileForm(request.POST, request.FILES,instance=manager)
		u_form = UserForm(request.POST, request.FILES,instance=user)

		if p_form.is_valid() and u_form.is_valid():
			p_form.save()
			u_form.save()
			messages.success(request,'Your Profile has been updated!')
			# return redirect('userprofile')
		else:
			messages.success(request,'The image is larger than 5 MB')	
		

	context ={'teams': teams, 'users':usersview, 'user': user, 'manager':manager, 'p_form':p_form, 'u_form':u_form}

	return render(request,'account/profile.html', context)


def viewmanager(request, user_id):
	usersview = Manager.objects.all() #navbar select
	users = User.objects.get(id=user_id)
	manager = Manager.objects.get(user=users)
	# manager = request.user.manager
	p_form = ProfileForm(instance=manager)
	u_form = UserForm(instance=users)

	teams = Team.objects.filter(manager_id=manager.id)

	context ={'teams': teams, 'users':usersview, 'user_form': users, 'manager':manager, 'p_form':p_form, 'u_form':u_form}

	return render(request,'account/viewprofile.html', context)

def all_managers(request):
	usersview = Manager.objects.all() #navbar select
	all_managers = Manager.objects.all()
	# teams=Team.get_all_teams().order_by('-Points')
	# name1='Page'
	# teams = Team.objects.filter(manager_id=usersview.id)

	home_data = { 'users':usersview, 'all_managers': all_managers, 
				# 'Select_team': teams, 'name_test': name1
				 }
	return render(request, 'account/managers.html', home_data)

# # # # # END User # # # # #  # # # # # # # # # # # # # # # # # # # # # # # # #

def leagues(request):
	usersview = Manager.objects.all() #navbar select
	name_torney = Season_name.objects.all().order_by('-date')
	# teams=Team.get_all_teams().order_by('-Points')
	# name1='Page'
	home_data = {'users':usersview, 'name_torney': name_torney, 
				# 'Select_team': teams, 'name_test': name1
				 }
	return render(request, 'weblog_app/leagues.html', home_data)

def tables(request, id):
	usersview = Manager.objects.all() #navbar select

	name_torney = Season_name.objects.all().order_by('-date')
	select_team = Team.objects.filter(season_name_id=id).order_by('-Points','-Score_result')
	team = name_torney.filter(id=id) #select name season  name
	
	# select matchs
	select_match = Match.objects.filter(season_name_id=id).order_by('-date')
	
	data = {'users':usersview, 'select_match' : select_match, 'select_team': select_team, 'name_torney':name_torney, 'Select_name': name_torney, 'team': team}
	
	return render(request,'weblog_app/tables.html', data)

def team(request, id):
	usersview = Manager.objects.all() #navbar select

	team = get_object_or_404(Team, pk=id)
	season_id = team.season_name
	# print(season_id)

	context ={'users':usersview, 'team':team}
	if request.user.is_authenticated:
		context['manager'] = request.user.manager



	return render(request,'weblog_app/team.html', context)

class TeamUpdate(UpdateView):
		model = Team 
		# id = model.id
		# team = get_object_or_404(Team, pk=id)
		template_name = "weblog_app/team_update_form.html"
		form_class = TeamUpdateForm
		def get_success_url(self):
			pk = self.kwargs["pk"]
			return reverse("team", kwargs={"id":pk})


class TeamDelete(DeleteView):
    model = Team 
    template_name = "weblog_app/team_delete_form.html"
    success_url = reverse_lazy('userprofile')

@login_required(login_url='login')
def new_team(request):
	usersview = Manager.objects.all() #navbar select

	# manager = request.user.manager.id
	manager = request.user.manager
	# manager = request.user
	# print(manager)
	context ={}
	form = TeamForm(request.POST)

	if form.is_valid():
		name_body = form.cleaned_data['name']
		season_body = form.cleaned_data['season_name']
		form = Team(manager=manager, season_name=season_body, name=name_body)
		form.save()
		messages.success(request,'Your Team has been created')
		return redirect("userprofile")

	context ={'users':usersview, 'form':form}

	return render(request, 'weblog_app/new_team.html', context)


# admin select team home

def get_team(request, season_name_id):
	teams = Team.objects.filter(season_name_id=season_name_id)
	return JsonResponse({'data': [{'id': Team_home.id, 'name': Team_home.name} for Team_home in teams]})

# --------------------------------------------------------------------------------
# ------------------ GMAIL ---------------------------------------------
# -----------------------------------------------------------------------------------

# import smtplib
 
# # list of email_id to send the mail
# 	li = ["lipnicanmilos@gmail.com", "follow-nails-72@docasnyemail.sk"]
	
# 	for dest in li:
# 		s = smtplib.SMTP('smtp.gmail.com', 587)
# 		s.starttls()
# 		s.login("webappflask0@gmail.com", "ilfcpbgrgchhppwg")
# 		message = "Message_you_need_to_send"
# 		s.sendmail("webappflask0@gmail.com", dest, message)
# 		s.quit()