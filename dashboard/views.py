from django.shortcuts import render, redirect


# Create your views here.
from features.models import Appointment
from user_model.models import Account


def patient_dashboard(request):
    return render(request, 'dashboard/patient_dashboard.html')


def doctor_dashboard(request):
    return render(request, 'dashboard/doctor_dashboard.html')
