from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FeedbackForm
from .models import FeedBack
from django.urls import reverse_lazy
# Create your views here.

class FormFeedback(CreateView):
    model=FeedBack
    form_class=FeedbackForm
    template_name='feedback/form.html'
    success_url=reverse_lazy('faculty:teachers')
    def form_valid(self,form):
        return super().form_valid(form)