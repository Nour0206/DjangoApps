from django.urls import path
from meetings import views

urlpatterns=[path ('getall/',views.meeting_list_view,name='meetings'),
             path('get/<int:id>/',views.meeting_detail_view,name='detail'),
             path('delete/<int:id>/',views.delete_meet,name='delete')]