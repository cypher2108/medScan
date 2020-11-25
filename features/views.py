from django.shortcuts import render, redirect

# Create your views here.
from features.models import Appointment, Prescription, Blogs
from user_model.models import Account
from features.forms import EditPatientProfileForm, EditDoctorProfileForm
from datetime import date


# patient features lies here
def patient_appointments_view(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    appointment = Appointment.objects.all()
    a = {'appointment': appointment}
    return render(request, 'features/patient/patient_appointments_view.html', a)


def patient_appointments_add(request):
    # return render(request, 'features/patient_appointments_add.html')
    error = ""
    if not request.user.is_authenticated:
        return redirect('patient_login')

    doctor1 = Account.objects.filter(is_doctor=True)
    patient1 = Account.objects.filter(is_doctor=False)

    if request.method == 'POST':
        d = request.POST['doc']
        # p = request.POST['pat']
        p = request.user.username
        status = "pending"
        date = request.POST['date']
        time = request.POST['time']
        doctor = Account.objects.filter(username=d).first()
        patient = Account.objects.filter(username=p).first()
        try:
            Appointment.objects.create(doctor_name=doctor, patient_name=patient, status=status, date=date,
                                       time=time)
            error = "no"
        except:
            error = "yes"
    x = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'features/patient/patient_appointments_add.html', x)


def patient_prescriptions(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    prescription = Prescription.objects.all()
    p = {'prescription': prescription}
    return render(request, 'features/patient/patient_prescriptions.html', p)


def edit_patient_profile(request):
    if request.method == 'POST':
        form = EditPatientProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'features/patient/edit-patient-profile.html')

    else:
        form = EditPatientProfileForm(instance=request.user)
        args = {'forms': form}
        return render(request, 'features/patient/edit-patient-profile.html', args)


def patient_medscan(request):
    return render(request, 'features/patient/patient-medscan.html')


# doctor features lies here
def doctor_prescription_view(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    prescription = Prescription.objects.all()
    p = {'prescription': prescription}
    return render(request, 'features/doctor/doctor_prescription/view_prescription.html', p)


def doctor_prescription_create(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('doctor_login')

    doctor1 = Account.objects.filter(is_doctor=True)
    patient1 = Account.objects.filter(is_patient=True)

    if request.method == 'POST':
        p = request.POST['pat']
        d = request.user.username
        symptoms = request.POST['symptoms']
        prescription = request.POST['prescpt']
        date = request.POST['date']
        print(date)

        doctor = Account.objects.filter(username=d).first()
        patient = Account.objects.filter(username=p).first()
        try:
            Prescription.objects.create(d_name=doctor, p_name=patient, date=date,
                                        symptoms=symptoms, prescription=prescription)
            error = "no"
        except:
            error = "yes"
    x = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'features/doctor/doctor_prescription/give_prescription.html', x)


def doctor_appointments(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    appointment = Appointment.objects.all()
    a = {'appointment': appointment}
    return render(request, 'features/doctor/doctor_appointments.html', a)


def create_blogs(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('doctor_login')

    doctor1 = Account.objects.filter(is_doctor=True)

    if request.method == 'POST':
        d = request.user.username
        title = request.POST['title']
        blog_body = request.POST['blog-body']
        date_today = date.today()

        doctor = Account.objects.filter(username=d).first()
        try:
            Blogs.objects.create(doc_name=doctor, date=date_today,
                                 heading=title, content=blog_body)
            error = "no"
        except:
            error = "yes"
    x = {'doctor': doctor1, 'error': error}
    return render(request, 'features/doctor/crate-blogs.html', x)


def edit_doctor_profile(request):
    if request.method == 'POST':
        form = EditDoctorProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'features/doctor/edit-doctor-profile.html')

    else:
        form = EditDoctorProfileForm(instance=request.user)
        args = {'forms': form}
        return render(request, 'features/doctor/edit-doctor-profile.html', args)


def patient_blogs(request):
    if not request.user.is_authenticated:
        return redirect('patient_login')
    blogs = Blogs.objects.all()
    p = {'posts': blogs}
    return render(request, 'features/patient/patient-blogs.html', p)
