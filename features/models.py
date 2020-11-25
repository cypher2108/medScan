from django.db import models

# Create your models here.
from user_model.models import Account


class Appointment(models.Model):
    doctor_name = models.ForeignKey(Account, related_name='doctor', on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Account, related_name='patient', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.doctor_name.first_name + "  " + self.patient_name.first_name


class Prescription(models.Model):
    d_name = models.ForeignKey(Account, related_name='d_name', on_delete=models.CASCADE)
    p_name = models.ForeignKey(Account, related_name='p_name', on_delete=models.CASCADE)
    date = models.DateField()
    symptoms = models.CharField(max_length=150)
    prescription = models.TextField(max_length=500)

    def __str__(self):
        return self.d_name.first_name + "  " + self.p_name.first_name


class Blogs(models.Model):
    doc_name = models.ForeignKey(Account, related_name='doc_name', on_delete=models.CASCADE)
    date = models.DateField()
    heading = models.CharField(max_length=150)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.doc_name.first_name + "  " + self.pat_name.first_name
