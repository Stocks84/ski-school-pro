from django.shortcuts import render
from .models import Lesson, Instructor

# Create your views here.

def home(request):
    return render(request, 'booking/home.html')

def lesson_list(request):
    # Retrieve all lessons from the database
    lessons = Lesson.objects.all()
    # Pass the lessons to the template for rendering
    return render(request, 'booking/lesson_list.html', {'lessons': lessons})


def instructor_list(request):
    instructors = Instructor.objects.all()  # Retrieve all instructors from the database
    return render(request, 'booking/instructor_list.html', {'instructors': instructors})


