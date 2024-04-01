from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Lesson, Instructor, Booking
from .forms import BookingForm, UserRegistrationForm, LessonForm, InstructorForm



# Create your views here.

def home(request):
    return render(request, 'booking/home.html')

@login_required
def lesson_list(request):
    """Retrieve all lessons from the database"""
    lessons = Lesson.objects.all()
    return render(request, 'booking/lesson_list.html', {'lessons': lessons})

def instructor_list(request):
    """Retrieve all instructors from the database"""
    instructors = Instructor.objects.all()
    return render(request, 'booking/instructor_list.html', {'instructors': instructors})

@login_required
def book_lesson(request, lesson_id=None):
    """Requires users to be logged in, allows the user to submit booking information, 
    saves the booking to the database, & displays a success message upon a successful booking."""
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
            return redirect('home') 
    else:
        form = BookingForm(instance=lesson)
    return render(request, 'booking/booking_form.html', {'form': form})


def register(request):
    """Saves user information to the database, & provides feedback to the user upon
    successful registration, also redirects to the homepage."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your registration was successful. You can now log in.')
            return redirect('home') 
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/registration_form.html', {'form': form})

def user_login(request):
    """Authenticating users, & provides feedback to the user upon successful or unsuccessful login attempts,
    redirects to home page on success."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'booking/login_form.html')

@login_required
def user_logout(request):
    """Handles user logout by ending the user's session and redirecting them to the home page."""
    logout(request)
    return redirect('home')

@login_required
def instructor_profile(request):
    """Check if the logged-in user is a ski instructor"""
    try:
        instructor = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        messages.error(request, 'SORRY YOU ARE NOT A INSTRUCTOR. PLEASE BOOK A LESSON')
        return redirect('home')

    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('instructor_profile')
    else:
        form = InstructorForm(instance=instructor)

    return render(request, 'booking/instructor_profile.html', {'form': form})

@login_required
def delete_instructor_profile(request):
    """Deletes the instructor profile. Ensures that only authenticated users who are registered
    instructors can delete their profiles. Provides feedback to the user upon successful deletion
    & redirects to the home page. A user who is not an instructor tries to access page, they are 
    notified that they cannot delete a profile they don't have."""
    try:
        instructor = Instructor.objects.get(user=request.user)
    except Instructor.DoesNotExist:
        messages.error(request, 'You are not a ski instructor.')
        return redirect('home')

    if request.method == 'POST':
        instructor.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home') 
    return render(request, 'booking/delete_instructor_profile.html')