from turtle import title
from django.contrib import admin
from .models import Post, Comment, Manager, Season_name, Team, Match
from django.contrib.auth.models import User
# from .forms import MyFormSet, MyForm
# from .forms import TeamInlineCustomFormSet, TeamInlineCustomForm
# from .forms import GameAdminForm
from dynamic_admin_forms.admin import DynamicModelAdminMixin

class Admin_post(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'author']
    search_fields = ['title', 'body']
    list_filter = ['author']

class Admin_mannager(admin.ModelAdmin):
     list_display = ['user_id', 'user']
    #  list_display = ['username', 'first_name', 'last_name', 'email', 'created', 'last_login', 'image']

    #  search_fields = ['username', 'first_name', 'last_name']
class Admin_comment(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'date', 'body']
    ordering = ['-post', '-date']
    list_filter = ['post', 'author']
#     search_fields = ['post', 'body']

class Admin_season_name(admin.ModelAdmin):
    list_display = ['name', 'date']

class Admin_team(admin.ModelAdmin):
    list_display = ['name', 'manager', 'season_name']
    ordering = ['season_name']
    list_filter = ['season_name']



# country --> season_name
# city --> Team_home
from .forms import Match_form


class Admin_match(admin.ModelAdmin):
    model = Match
    form = Match_form
    fields = ['season_name', 'Team_home', 'Team_visitor', 'Team_home_goal', 'Team_visitor_goal', 'date', 'body']
    list_display = ('date', 'season_name', 'Team_home', 'Team_visitor')



    def get_fields(self, request, obj:None):
        fields = super().get_fields(request, obj)
        fields.remove('season_name')
        fields.insert(fields.index('Team_home'),'season_name')

        return fields

    class Media:
        js = (
            "js/chained.js",
        )



        # self.__original_name = self.name

    # form = SomeModelForm
    # formset = TeamInlineCustomFormSet
    # form = TeamInlineCustomForm
    # formset = MyFormSet

# ------------------- prepis nazvu 
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["season_name"].label = "season_name (Vyber turnaj):"
    #     return form
# # -------------------- funkcne z 3 
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         qs = super().get_queryset(request)
#         # print(self.fields)
#         # super (MyFormSet, self).__init__(self, **kwargs)
#         if db_field.name == "Team_home":
#             kwargs["queryset"] = Team.objects.filter(season_name__id=3)
#         return super(Admin_match, self).formfield_for_foreignkey(db_field, request, **kwargs)
# # -----------------------
# ------------------------


# Register your models here.
admin.site.register(Manager, Admin_mannager)
admin.site.register(Post, Admin_post)
admin.site.register(Comment, Admin_comment)
admin.site.register(Season_name, Admin_season_name)
admin.site.register(Team, Admin_team)
admin.site.register(Match, Admin_match)



