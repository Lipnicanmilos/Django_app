from django.urls import path
from weblog_app import views

urlpatterns = [
    # admin select team
    path('Team_home/list/<season_name_id>', views.get_team),
]