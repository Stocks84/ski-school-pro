from django.test import TestCase
from .forms import InstructorForm, BookingForm


class TestBookingForm(TestCase):
    """Test for the 'lesson' field"""
    def test_lesson_is_required(self):
        booking_form = BookingForm({
            'lesson': '',
            'student': 'Stocks84'
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg="Lesson was not provided, but the form is valid"
        )

    def test_student_is_required(self):
        """Test for the student field"""
        booking_form = BookingForm({
            'lesson': '1',
            'student': ''
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg="Student was not provided, but the form is valid"
        )



class TestInstructorForm(TestCase):
    """Test for the 'bio' field"""
    def test_form_is_valid(self):
        instructor_form = InstructorForm({'bio': 'hello this is a bio'})
        self.assertTrue(instructor_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        instructor_form = InstructorForm({'bio': ''})
        self.assertFalse(instructor_form.is_valid(), msg="Form is valid" )