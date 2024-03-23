# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('book-lesson/', views.book_lesson, name='book_lesson'),
]

