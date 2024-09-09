from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,r'HospitalSystem\reg.html',context)
    
# Create your views here.

@login_required
def index(request):
    return render(request, "HospitalSystem/index.html")

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'HospitalSystem/login.html')

def search_doctors(request):
    specialty = request.GET.get('specialty', '')
    location = request.GET.get('location', '')

    doctors = Doctor.objects.all()

    if specialty:
        doctors = doctors.filter(specialty__icontains=specialty)
    if location:
        doctors = doctors.filter(location__icontains=location)

    return render(request, 'HospitalSystem/index.html', {'doctors': doctors})










