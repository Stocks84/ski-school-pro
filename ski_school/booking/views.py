from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Lesson, Instructor, Booking
from .forms import BookingForm, UserRegistrationForm, LessonForm, InstructorForm

# Create your views here.

def home(request):
    return render(request, 'booking/home.html')

@login_required
def lesson_list(request):
    # Retrieve all lessons from the database
    lessons = Lesson.objects.all()
    # Pass the lessons to the template for rendering
    return render(request, 'booking/lesson_list.html', {'lessons': lessons})

def instructor_list(request):
    instructors = Instructor.objects.all()  # Retrieve all instructors from the database
    return render(request, 'booking/instructor_list.html', {'instructors': instructors})

@login_required
def book_lesson(request, lesson_id=None):
    lesson = None
    if lesson_id:
        lesson = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=lesson)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your lesson has been booked successfully!')
            return redirect('home')  # Redirect to a success page
    else:
        form = BookingForm(instance=lesson)
    return render(request, 'booking/booking_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your registration was successful. You can now log in.')
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/registration_form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'booking/login_form.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def instructor_profile(request):
    instructor = Instructor.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('instructor_profile')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'booking/instructor_profile.html', {'form': form})

