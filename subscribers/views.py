from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render,redirect
# Create your views here.
def SubscriberView(request):
	new_subscriber = subscriber(email =request.POST['email'])
	new_subscriber.save()
	return redirect('menu:home')





