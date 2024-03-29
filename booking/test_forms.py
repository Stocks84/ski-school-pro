from django.test import TestCase
from .forms import InstructorForm


class TestInstructorForm(TestCase):

    def test_form_is_valid(self):
        instructor_form = InstructorForm({'bio': 'hello im great'})
        self.assertTrue(instructor_form.is_valid())