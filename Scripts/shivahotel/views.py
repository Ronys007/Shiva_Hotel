from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
# Create your views here.

def home(request):
    if Booking:
        book= Booking.objects.all()
    return render(request,'home.html', {'book':book})