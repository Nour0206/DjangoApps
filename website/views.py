from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.
def home_view(request):
    context={'nbre_meeting': Meeting.objects.count()}
    return render(request,"website/home.html",context=context)

def about_view(request):
 return render(request,"website/about.html")

def meetings_list_view(request):
 meetings=Meeting.objects.all()
 meetings={'meetings':meetings}
 return render(request,"website/meetings.html",{'metings':meetings,})



