from django.contrib import admin
from django.urls import path
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout_view'),
    path('register/', user_register, name='register'),
    # path('forgot_password/', forgot_password, name='forgot_password'),
    # path('test/', test, name='test'),
    # Login Mahasiswa
    path('register-mahasiswa/', mhs_register, name='mhs_register'),
    path('login-mahasiswa/', mhs_login, name='login_mhs'),
]
