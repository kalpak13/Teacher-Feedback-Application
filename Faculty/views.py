from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from .forms import NewTeacherForm
from django.urls import reverse,reverse_lazy
from .models import Teacher

# Create your views here.

class NewTeacher(CreateView):
    template_name='faculty/new_teacher.html'
    form_class=NewTeacherForm
    success_url=reverse_lazy('faculty:teachers')


class Teachers(ListView):
    template_name='faculty/teachers.html'
    context_object_name='teachers'
    model=Teacher


class TeacherProfile(DetailView):
    template_name='faculty/teacher_profile.html'
    context_object_name='profile'
    model=Teacher

class RemoveTeacher(DeleteView):
    template_name='faculty/remove_teacher.html'
    model=Teacher
    success_url=reverse_lazy('faculty:teachers')
    context_object_name='teacher'

class UpdateProfile(UpdateView):
    model=Teacher
    template_name='faculty/update_profile.html'
    fields=('__all__')
    success_url=reverse_lazy('faculty:teachers')


