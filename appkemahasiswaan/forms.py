from django.forms import ModelForm, forms
from django import forms
from appkemahasiswaan.models import *

class FormArtikel(ModelForm):
    class Meta:
        model = Artikel
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'publikasi': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'Deskripsi': forms.Textarea({'class': 'form-control', 'placeholder': 'Tuliskan deskripsi artikel'}),
            'kategori': forms.TextInput({'class': 'form-control', 'placeholder': 'Maksukkan Kategori'}),
            'image': forms.ClearableFileInput({'class': 'form-control', 'id': 'upload-image', 'accept': 'image/*', 'onchange': 'previewImage(event)'}),
        }

class FormPrestasi(ModelForm):
    class Meta:
        model = Prestasi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'prestasi': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Prestasi Mahasiswa'}),
            'penyelenggara': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan penyelenggara'}),
            'tanggal': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'tingkat': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Tingkat Perlombaan'}),
            'juara': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Juara Ke-'}),
            'gender': forms.Select({'class': 'form-control'}),
        }

class FormPelanggaran(ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'angkatan': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Angkatan'}),
            'Jenis_pelanggaran': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Jenis Pelanggaran Yang Dilakukan'}),
            'sanksi': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Sanksi Yang di Dapatkan'}),
            'gender': forms.Select({'class': 'form-control'}),
        }

class FormDataBeasiswa(ModelForm):
    class Meta:
        model = Data_Beasiswa
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Beasiswa'}),
            'dibuka': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'ditutup': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'benefit': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Benefit Yang Diterima'}),
            'deskripsi': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Deskripsi Beasiswa'}),
            'persyaratan': forms.Textarea({'class': 'form-control', 'placeholder': 'Masukkan Persyaratan Beasiswa'}),
            'ip_minimal': forms.NumberInput({'class': 'form-control', 'placeholder': 'IP Minimal '}),
            'ipk_minimal': forms.NumberInput({'class': 'form-control', 'placeholder': 'IPK Minimal '}),
            'status': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Status Beasiswa'}),
            'image': forms.ClearableFileInput({'class': 'form-control'}),
        }

class FormPenerima_Beasiswa(ModelForm):
    class Meta:
        model = Penerima_Beasiswa
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'angkatan': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Angkatan'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'beasiswa': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Beasiswa'}),
            'status': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Status Mahasiswa'}),
            'gender': forms.Select({'class': 'form-control'}),
        }

class FormMahasiswa_Magang(ModelForm):
    class Meta:
        model = Mahasiswa_Magang
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'angkatan': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Angkatan'}),
            'jalur_masuk': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Jalur Masuk'}),
            'tgl_magang': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'perusahaan': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Perusahaan'}),
            'pembimbing': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Pembimbing Title & Gelar'}),
            'semester': forms.Select({'class': 'form-control'}),
            'gender': forms.Select({'class': 'form-control'}),
        }

class Form_Organisasi(ModelForm):
    class Meta:
        model = Organisasi
        fields = '__all__'

        widgets = { 
            'organisasi': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Organisasi'}),
            'visi': forms.Textarea({'class': 'form-control', 'placeholder': 'Visi Organisasi'}),
            'misi': forms.Textarea({'class': 'form-control', 'placeholder': 'Misi Organisasi'}),
            'logo': forms.ClearableFileInput({'class': 'form-control'}),
            'status': forms.Select({'class': 'form-control'}),
        }

class Form_Anggota_Organisasi(ModelForm):
    class Meta:
        model = Anggota_Organisasi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan NIM Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Mahasiswa'}),
            'prodi': forms.Select({'class': 'form-control'}),
            'angkatan': forms.NumberInput({'class': 'form-control', 'placeholder': 'Masukkan Angkatan'}),
            'organisasi': forms.Select({'class': 'form-control'}),
            'jabatan': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Jabatan'}),
            'foto': forms.ClearableFileInput({'class': 'form-control'}),
            'gender': forms.Select({'class': 'form-control'}),
        }