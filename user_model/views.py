from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from user_model.models import Account


def login_as(request):
    return render(request, 'user_model/login_as.html')


def register_as(request):
    return render(request, 'user_model/register_as.html')


def patient_sign_in(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_model/patient_login.html', d)


def doctor_sign_in(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_model/doctor_login.html', d)


def sign_out(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')


def patient_register(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email_address = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        try:
            if password == confirm_password:
                user = Account.objects.create_user(username=username, email=email_address, password=password)
                user.is_doctor = False
                user.is_patient = True
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'user_model/patient_sign_up.html', p)


def doctor_register(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        email_address = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        try:
            if password == confirm_password:
                user = Account.objects.create_user(username=username, email=email_address, password=password)
                user.is_doctor = True
                user.is_patient = False
                user.save()
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    p = {'error': error}
    return render(request, 'user_model/doctor_sign_up.html', p)
