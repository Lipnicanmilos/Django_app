"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weblog_app import views
from django.contrib.auth import views as auth
from . import settings
from django.conf.urls.static import static

# from django.conf.urls import url, include

# admin site
admin.site.site_header = "Admin Dashboard"
admin.site.index_title = "Admin"
admin.site.site_title = "Tournament"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dynamic-admin-form/", include("dynamic_admin_forms.urls")),
    path('', views.index, name='index'),
    # path('', views.base, name='base'),
    path('', include("django.contrib.auth.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('blog/', include('weblog_app.urls')),
    path('chaining/', include("smart_selects.urls")),

    path('post/<int:post_id>/', views.post, name='post'),
    path('post/create', views.PostCreate.as_view(), name="createpost"),
    path('post/update/<int:pk>', views.PostUpdate.as_view(), name="updatepost"),
    path('post/delete/<pk>', views.PostDelete.as_view(), name="deletepost"),
    path('post/<int:post_id>/addcomment', views.addcomment, name='addcomment'),
    
    path('search', views.search, name='search'),
    path('livesearch/<str:word>/<int:sid1>.<int:sid2>', views.livesearch, name='livesearch'),
    
    path("register/", views.register_request, name="register"),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_view, name='logout'),
    
    path('profile/', views.userprofile, name='userprofile'),
    path('managers/<int:user_id>', views.viewmanager, name='viewmanager'),
    path('managers', views.all_managers, name='managers'),

    path('leagues', views.leagues, name='leagues'),
    path('leagues/<int:id>/', views.tables, name='tables'),

    path('team/<int:id>', views.team, name='team'),
    path('team/update/<int:pk>', views.TeamUpdate.as_view(), name="updateteam"),
    path('team/delete/<int:pk>', views.TeamDelete.as_view(), name="deleteteam"),
    path('team', views.new_team, name='new_team'),

    # path('manager/<int:user_id>/', views.manager, name='manager'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


