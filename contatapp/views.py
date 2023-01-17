from django.shortcuts import render
from . import forms
from .forms import contactform

# Create your views here.



def index(request):
    cform=contactform()
    if cform.is_valid():
        cform.save()
    return  render(request,'cform.html',{'cform':cform})


