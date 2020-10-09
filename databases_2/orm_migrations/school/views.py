from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    teachers = Teacher.objects.prefetch_related('students').all()
    context = {'object_list': teachers}
    return render(request, template, context)
