from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# booking/models.py

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration_hours = models.IntegerField()
    max_students = models.IntegerField()

    def __str__(self):
        return f"{self.instructor} - {self.date} {self.time}"


class Booking(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.lesson}"
