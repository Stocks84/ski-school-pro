from .models import Instructor

def instructors(request):
    return {'instructors': Instructor.objects.all()}