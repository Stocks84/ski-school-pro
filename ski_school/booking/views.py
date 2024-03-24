from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lesson, Instructor, Booking
from .forms import BookingForm
from .forms import UserRegistrationForm

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


def book_lesson(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations your Registration was a success! You can now log in.')
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/registration_form.html', {'form': form})


