from django.forms import ModelForm, forms
from django import forms
from .models import *

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput({'class': 'form-control', 'placeholder': 'Nama depan'}),
            'last_name': forms.TextInput({'class': 'form-control', 'placeholder': 'Nama belakang'}),
            'gender': forms.Select({'class': 'form-control'}),
            'tgl_lahir': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'status': forms.TextInput({'class': 'form-control', 'placeholder': 'Status'}),
            'warga_negara': forms.TextInput({'class': 'form-control', 'placeholder': 'Warga Negara'}),
            'agama': forms.TextInput({'class': 'form-control', 'placeholder': 'Agama'}),
            'alamat': forms.TextInput({'class': 'form-control', 'placeholder': 'Alamat'}),
            'email': forms.TextInput({'class': 'form-control', 'placeholder': 'email@gmail.com', 'type':'email'}),
            'nomer_hp': forms.TextInput({'class': 'form-control', 'placeholder': 'Nomor tlp bisa dihubungi', 'type':'number'}),
            'photo': forms.ClearableFileInput({'class': 'form-control'}),
            'deskripsi': forms.Textarea({'class': 'form-control', 'placeholder': 'tuliskan deskripsi diri anda'}),
        }

class PendidikanForm(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = '__all__'

        widgets = {
            'personal_info': forms.TextInput({'class': 'form-control', 'value': '{{ personal_info.first_name }} {{ personal_info.last_name }}'}),
            'nama_pendidikan': forms.TextInput({'class': 'form-control', 'placeholder': 'Sekolah / Institusi / Universitas'}),
            'masuk': forms.TextInput({'class': 'form-control', 'placeholder': 'tahun masuk', 'type':'number'}),
            'tamat': forms.TextInput({'class': 'form-control', 'placeholder': 'tahun keluar', 'type':'number'}),
            'jenjang': forms.TextInput({'class': 'form-control', 'placeholder': 'jenjang pendidikan'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

        widgets = {
            'bidang': forms.TextInput({'class': 'form-control', 'placeholder': 'bidang dikuasai'}),
            'keterangan': forms.TextInput({'class': 'form-control', 'placeholder': 'keahlian yang dimiliki'}),
        }

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

        widgets = {
            'training': forms.TextInput({'class': 'form-control', 'placeholder': 'trainig/seminar'}),
            'tahun': forms.TextInput({'class': 'form-control', 'placeholder': 'tahun trainig/seminar', 'type':'number'}),
            'penyelenggara': forms.TextInput({'class': 'form-control', 'placeholder': 'penyelenggara trainig/seminar'}),
        }

# class ProfilForm(forms.ModelForm):
#     class Meta:
#         model = ProfilMahasiswa
#         fields = ['prodi', 'tmp_lahir', 'tgl_lahir', 'gender', 'Agama', 'alamat', 'nomer_hp', 'bio', 'foto']

# class PersonalInfoForm(forms.ModelForm):
#     class Meta:
#         model = PersonalInfo
#         exclude = ('cv',)

# class PendidikanForm(forms.ModelForm):
#     class Meta:
#         model = Pendidikan
#         exclude = ('cv',)

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         exclude = ('cv',)

# class TrainingForm(forms.ModelForm):
#     class Meta:
#         model = Training
#         exclude = ('cv',)

class SkpiForm(forms.ModelForm):
    class Meta:
        model = data_skpi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'nama': forms.TextInput({'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'tempat': forms.TextInput({'class': 'form-control', 'placeholder': 'Tempat Lahir'}),
            'tgl_lahir': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'masuk': forms.NumberInput({'class': 'form-control', 'placeholder': 'Tahun Masuk'}),
            'lulus': forms.NumberInput({'class': 'form-control', 'placeholder': 'Tahun Lulus'}),
            'ppi': forms.TextInput({'class': 'form-control', 'placeholder': 'Program Praktik Industri'}),
            'PA': forms.TextInput({'class': 'form-control', 'placeholder': 'Judul Proyek Akhir'}),
            'foto': forms.ClearableFileInput({'class': 'form-control', 'onchange': 'previewImage(event)'}),
            'prodi': forms.Select({'class': 'form-control'}),
        }

class OrganisasiForm(forms.ModelForm):
    class Meta:
        model = organisasi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'kegiatan': forms.TextInput({'class': 'form-control', 'placeholder': 'Organisasi / Kegiatan MBKM'}),
            'penempatan': forms.TextInput({'class': 'form-control', 'placeholder': 'Jabatan / Penempatan'}),
            'periode': forms.TextInput({'class': 'form-control', 'placeholder': 'waktu / periode'}),
        }

class PelatihanForm(forms.ModelForm):
    class Meta:
        model = pelatihan
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'pelatihan': forms.TextInput({'class': 'form-control', 'placeholder': 'Pelatihan / Seminar'}),
            'pelaksana': forms.TextInput({'class': 'form-control', 'placeholder': 'Pelaksana'}),
            'periode': forms.TextInput({'class': 'form-control', 'placeholder': 'waktu / periode'}),
        }

class PenghargaanForm(forms.ModelForm):
    class Meta:
        model = penghargaan
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'penghargaan': forms.TextInput({'class': 'form-control', 'placeholder': 'Kegiatan / Penghargaan'}),
            'prestasi': forms.TextInput({'class': 'form-control', 'placeholder': 'Juara II, Juara II atau Juara III'}),
            'periode': forms.TextInput({'class': 'form-control', 'placeholder': 'waktu / periode'}),
        }

class SertifikasiForm(forms.ModelForm):
    class Meta:
        model = sertifikasi
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'bidang': forms.TextInput({'class': 'form-control', 'placeholder': 'Bidang / Kompetensi'}),
            'no_sertifikat': forms.TextInput({'class': 'form-control', 'placeholder': 'Xxx/Xx/xx'}),
            'penerbit': forms.TextInput({'class': 'form-control', 'placeholder': 'Penerbit'}),
        }

class BeasiswaForm(forms.ModelForm):
    class Meta:
        model = beasiswa
        fields = '__all__'

        widgets = {
            'nim': forms.NumberInput({'class': 'form-control', 'placeholder': 'Nomor Induk Mahasiswa'}),
            'beasiswa': forms.TextInput({'class': 'form-control', 'placeholder': 'Beasiswa'}),
            'pemberi': forms.TextInput({'class': 'form-control', 'placeholder': 'Pemberi Beasiswa'}),
            'periode': forms.TextInput({'class': 'form-control', 'placeholder': 'Periode'}),
        }