from django.shortcuts import render, get_object_or_404
from .models import Track

# Create your views here.

def track_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Track.objects.create(name=name)

    tracks = Track.objects.all()
    return render(request, 'tracks/track_list.html', {'tracks': tracks})
def show_students(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    students = track.students.all()
    return render(request, 'tracks/show_students.html', {'track': track, 'students': students})
