from django.shortcuts import render
from .models import Lesson

# Create your views here.

def home(request):
    return render(request, 'booking/home.html')

def lesson_list(request):
    # Retrieve all lessons from the database
    lessons = Lesson.objects.all()
    # Pass the lessons to the template for rendering
    return render(request, 'booking/lesson_list.html', {'lessons': lessons})

