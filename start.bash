source venv/Scripts/Activate
cd blog
./manage.py runserver


pip install django-jazzmin
pip install django-ckeditor
pip install django-dynamic-admin-forms
pip install django-crispy-forms

# Username: Admin
# Email address: milos@milos.sk
# # Admin36

# Milos
# Admin_123

# Ferko
# ferko@ferko.sk
# Admin_123

# Juraj
# 12_He_slo

# --sign up register 
# --login 
# --admin
# --profil
Tournament
search

    # path('admin/', admin.site.urls), ---
    # path("dynamic-admin-form/", include("dynamic_admin_forms.urls")),
    # path('', views.index, name='index'),
    # path('', views.base, name='base'),
    # path('', include("django.contrib.auth.urls")),
    # path('ckeditor/', include('ckeditor_uploader.urls')),

    path('blog/', include('weblog_app.urls')),
    path('chaining/', include("smart_selects.urls")),

    path('post/<int:post_id>/', views.post, name='post'),
    # path('post/create', views.PostCreate.as_view(), name="createpost"),
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
