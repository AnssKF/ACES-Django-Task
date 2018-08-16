from django.urls import path
from . import views


from .models import About

urlpatterns = [
	path('',views.index),
]