from django.urls import path
from . import views
#domain.com/website/...
urlpatterns=[
path('about',views.about_view, name='about'),
path('home',views.home_view, name='home'),
path('meetings',views.meetings_list_view, name='meetings_list'),
]