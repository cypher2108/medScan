from django.contrib import admin

# Register your models here.
from features.models import *

admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Blogs)
