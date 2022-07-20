from django.shortcuts import render
from django.views.generic import CreateView,View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse
from .models import School,Student
from django.urls import reverse_lazy
# Create your views here.
# def Index(request):`
#     return render(request,'basic_app/home.html')


# class Index(View):
    # def get(self,request):
        # return HttpResponse("this is cool-ish")

class Index(TemplateView):
    template_name='basic_app/home.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] ='this data is injected from CBV!' 
        return context
           


class SchoolListView(ListView):
    context_object_name='Schools'
    model=School
    


class SchoolDetailView(DetailView):
    model=School
    template_name='basic_app/school_detail.html'   
    context_object_name="school_details"


class SchoolCreateView(CreateView):
    fields=('name','principal','location')   
    # field is important and required attribute which allow user to fill only required fields of a model/form 
    model=School


class SchoolUpdateView(UpdateView):
    fields=('name','principal') 
    model=School


class SchoolDeleteView(DeleteView):
    model=School
    success_url=reverse_lazy("basic_app:list") 
    # use of success_url:- when successfully deleted go to this url

