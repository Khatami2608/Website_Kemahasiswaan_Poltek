from django.forms import ModelForm, forms
from django import forms
from appkemahasiswaan.models import *
from ckeditor.widgets import CKEditorWidget

class FormArtikel(ModelForm):
    Deskripsi = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Artikel
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'publikasi': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'kategori': forms.Select({'class': 'form-control'}),
            'image': forms.ClearableFileInput({'class': 'form-control', 'id': 'upload-image', 'accept': 'image/*', 'onchange': 'previewImage(event)'}),
            'status': forms.Select({'class': 'form-control'}),
        }


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'kategori': forms.TextInput({'class': 'form-control', 'placeholder': 'Buat kategori Baru'}),
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
            'ip_minimal': forms.TextInput({'class': 'form-control', 'placeholder': 'IP Minimal '}),
            'ipk_minimal': forms.TextInput({'class': 'form-control', 'placeholder': 'IPK Minimal '}),
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
            'status': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Status Mahasiswa'}),
            'gender': forms.Select({'class': 'form-control'}),
            'foto': forms.ClearableFileInput({'class': 'form-control', 'onchange': 'previewImage(event)'}),
        }

class FormBeasiswa(ModelForm):
    class Meta:
        model = Beasiswa
        fields = '__all__'

        widgets = {
            'beasiswa': forms.TextInput({'class': 'form-control', 'placeholder': 'Masukkan Nama Beasiswa'}),
            'smstr_awal': forms.TextInput({'class': 'form-control', 'placeholder': 'dari semester ke-'}),
            'smstr_akhir': forms.TextInput({'class': 'form-control', 'placeholder': 'sampai semester ke-'}),
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
            'perusahaan': forms.Select({'class': 'form-control'}),
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

class FormProdi(ModelForm):
    class Meta:
        model = Prodi
        fields = '__all__'

        widgets = {
            'prodi': forms.TextInput({'class': 'form-control', 'placeholder': 'Nama Program Studi'}),
            'ka_prodi': forms.TextInput({'class': 'form-control', 'placeholder': 'Nama Ketua Program Studi'}),
            'nrp': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor NRP'}),
        } 

class FormPerusahaan(ModelForm):
    deskripsi = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Perusahaan_PPI
        fields = '__all__'

        widgets = {
            'nama_psh' : forms.TextInput({'class': 'form-control', 'placeholder': 'Nama Perusahaan'}),
            'alamat' : forms.TextInput({'class': 'form-control', 'placeholder': 'Alamat Perusahaan'}),
            'email' : forms.TextInput({'class': 'form-control', 'placeholder': 'email@gmail.com', 'type':'email'}),
            'kontak' : forms.TextInput({'class': 'form-control', 'placeholder': 'Kontak Perusahaan', 'type':'number'}),
        }