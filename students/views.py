from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from tracks.models import Track

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def create_student(request):
    tracks = Track.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        track_id = request.POST['track']
        image = request.FILES.get('image')

        track = Track.objects.get(id=track_id)
        Student.objects.create(
            name=name,
            age=age,
            date_of_birth=date_of_birth,
            track=track,
            image=image
        )
        return redirect('student_list')

    return render(request, 'students/create_student.html', {'tracks': tracks})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    tracks = Track.objects.all()
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.date_of_birth = request.POST['date_of_birth']
        student.track_id = request.POST['track']
        if request.FILES.get('image'):
            student.image = request.FILES['image']
        student.save()
        return redirect('student_list')
    return render(request, 'students/update_student.html', {'student': student, 'tracks': tracks})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
