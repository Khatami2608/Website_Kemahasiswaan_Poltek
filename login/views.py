from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from appkemahasiswaan.models import *
from django.core.paginator import Paginator

# Proses Login Web Admin
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print("User successfully logged in:", user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password.')
                print("Login failed:", form.errors)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user.set_password(password)  # Setel kata sandi pengguna
            user.save()  # Simpan pengguna ke database
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Data berhasil disimpan.')
                return redirect('login')
        else:
            messages.error(request, 'Periksa Kembali !!.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



# @login_required(login_url='login')
def dashboard(request):
    ordering = '-publikasi'
    tb_artikel = Artikel.objects.all().order_by(ordering)
    paginator = Paginator(tb_artikel, 2) 

    konteks = {
        'tb_artikel': tb_artikel,
    }
    return render(request, 'dashboard/dashboard.html', konteks)

def user_logout (request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    kontext = {}
    return render(request, 'forgot-password.html', kontext)

# Proses Login Web Mahasiswa
def mhs_register(request):
    if request.method == 'POST':
        form = MahasiswaRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            nim = form.cleaned_data['nim']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(request, nim=nim, name=name, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Data berhasil disimpan')
                return redirect('home')
        else:
            messages.error(request, 'Periksa Kembali !!')
    else:
        form = MahasiswaRegistrationForm()
    return render(request, 'mahasiswa/register.html', {'form': form})

def mhs_login(request):
    if request.method == 'POST':
        form = MahasiswaLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print("Sukses Melakukan Login", user)
                return redirect('home')
            else:
                form.add_error(None, 'username atau password tidak benar!')
                print("login failed:", form.errors)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = MahasiswaLoginForm()
    return render(request, 'mahasiswa/login.html', {'form': form})