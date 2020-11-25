from django.urls import path

from features import views

urlpatterns = [
    path('auth/patient/patient_dashboad/appointments_view', views.patient_appointments_view,
         name='patient_appointments_view'),
    path('auth/patient/patient_dashboad/appointments_add', views.patient_appointments_add,
         name='patient_appointments_add'),
    path('auth/doctor/patient_dashboad/prescriptions', views.patient_prescriptions,
         name='patient_prescriptions'),
    path('auth/patient/patient_dashboard/my-profile/edit', views.edit_patient_profile,
         name='patient_profile'),
    path('auth/patient/patient_dashboard/medscan', views.patient_medscan,
         name='patient_medscan'),
    path('auth/patient/patient_dashboard/blogpost', views.patient_blogs,
         name='patient_blogs'),

    #     doctor urls starts here

    path('auth/doctor/doctor_dashboad/appointments_view', views.doctor_appointments,
         name='doctor_appointments_view'),
    path('auth/doctor/doctor_dashboard/prescription/view_prescription', views.doctor_prescription_view,
         name='doctor_prescription_view'),
path('auth/doctor/doctor_dashboard/prescription/give_prescription', views.doctor_prescription_create,
         name='doctor_prescription_give'),
    path('auth/doctor/doctor_dashboard/create_blogs', views.create_blogs,
         name='create_blogs'),
    path('auth/doctor/doctor_dashboard/my-profile/edit', views.edit_doctor_profile,
         name='doctor_profile'),

]
