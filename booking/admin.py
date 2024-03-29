from django.contrib import admin
from .models import Booking, Lesson, Instructor
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    search_fields = ['instructor']
    list_filter = ('time',)

@admin.register(Instructor)
class InstructorAdmin(SummernoteModelAdmin):
    summernote_fileds = ('bio',)

admin.site.register(Booking)
