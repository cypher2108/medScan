from django.urls import path

from user_model import views

urlpatterns = [
    path('create_user/patient_register/', views.patient_register, name='patient_register'),
    path('create_user/doctor_register/', views.doctor_register, name='doctor_register'),
    path('auth/patient_login/', views.patient_sign_in, name='patient_login'),
    path('auth/doctor_login/', views.doctor_sign_in, name='doctor_login'),
    path('authentication/auth_choice/', views.login_as, name='login_as'),
    path('create_user/', views.register_as, name='register_as'),
    path('logout/', views.sign_out, name='logout'),
]