from django.shortcuts import render
from django.http import HttpResponse

from .models import About

def index(request):
	data=About.objects.get(title='About')
	return render(request,'about.html' , {'data' : data})

