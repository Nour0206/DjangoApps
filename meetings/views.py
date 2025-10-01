from django.shortcuts import render

from meetings.models import Meeting
from django.shortcuts import get_object_or_404

# get all meetings.
def meeting_list_view(request):
    meetings=Meeting.objects.all()
    return render(request,"meetings.html",{'meetings':meetings})


# get meeting by id.
def meeting_detail_view(request,id):
    meeting=get_object_or_404(Meeting,id=id)
    return render(request,"detail.html",{'meeting':meeting})



def delete_meet(request , id):
    meeting = get_object_or_404(Meeting, id=id)
    if request.method =="POST":
        meeting.delete()
        return redirect('meetings')
    return render(request, 'confirm_delete.html', {'meeting':meeting})


