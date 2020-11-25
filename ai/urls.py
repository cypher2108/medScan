from django.urls import path

from ai import views

urlpatterns = [
    path('studyImage/', views.studyImage, name='studyImage')
]