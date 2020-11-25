from django.urls import path

from dashboard import views

urlpatterns = [
    path('auth/patient/patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('auth/doctor/doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
