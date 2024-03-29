from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Lesson, Instructor

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['lesson', 'student']  


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['instructor', 'date', 'time', 'duration_hours', 'max_students']  # Add more fields as needed


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['bio']

