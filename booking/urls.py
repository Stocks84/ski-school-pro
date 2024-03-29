# booking/urls.py
from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('book-lesson/', views.book_lesson, name='book_lesson'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('instructor/profile/', views.instructor_profile, name='instructor_profile'),
    path('instructor/profile/delete/', views.delete_instructor_profile, name='delete_instructor_profile'),
]