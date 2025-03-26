from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'crud_app/home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        roll_number = request.POST['roll_number']
        course = request.POST['course']
        Student.objects.create(name=name, email=email, roll_number=roll_number, course=course)
        return redirect('home')

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.roll_number = request.POST['roll_number']
        student.course = request.POST['course']
        student.save()
        return redirect('home')
    return render(request, 'crud_app/edit_student.html', {'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('home')

def delete_confirmation(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('home')
    return render(request, 'crud_app/delete_confirmation.html', {'student': student})
