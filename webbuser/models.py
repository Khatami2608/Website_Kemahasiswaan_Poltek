from django.db import models
from login.models import *
from appkemahasiswaan.models import *
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser

# class Cv(models.Model):
#     user = models.OneToOneField(user_mahasiswa, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username
class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    )  

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    tgl_lahir = models.DateField()
    status = models.CharField(max_length=20)
    warga_negara = models.CharField(max_length=50)
    agama = models.CharField(max_length=50)
    alamat = models.TextField()
    email = models.EmailField()
    nomer_hp = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='foto_cv/')
    deskripsi = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pendidikan(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    nama_pendidikan = models.CharField(max_length=100)
    masuk = models.PositiveIntegerField()
    tamat = models.PositiveIntegerField()
    jenjang = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_pendidikan}, {self.jenjang}"

class Skill(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE) 
    bidang = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bidang}, {self.keterangan}"

class Training(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    training = models.CharField(max_length=150)
    tahun = models.PositiveIntegerField()
    penyelenggara = models.CharField(max_length=100)

    def __str__(self):
        return self.training


GENDER_CHOICES = [
    ('laki-laki', 'Laki-Laki'),
    ('perempuan', 'Perempuan'),
]
User = get_user_model()

class ProfilMahasiswa(models.Model):
    user = models.OneToOneField(user_mahasiswa, on_delete=models.CASCADE)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    tmp_lahir = models.CharField(max_length=30)
    tgl_lahir = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    Agama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=150)
    nomer_hp = models.CharField(max_length=15)
    bio = RichTextField(blank=True, null=True)
    foto = models.ImageField(upload_to='mahasiswa/', null=True)

    def __str__(self):
        return self.user.email

GENDER_CHOICES = (
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
)
PRODI_CHOICES = (
    ('Teknik Informasi', 'Teknik Informasi'),
    ('Teknik Mekatronika', 'Teknik Mekatronika'),
    ('Teknologi Elektronika', 'Teknologi Elektronika'),
    ('Akuntansi', 'Akuntansi'),
    ('Akuntansi Sektor Publik', 'Akuntansi Sektor Publik'),
)
class data_skpi(models.Model):
    nim = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    tempat = models.CharField(max_length=30)
    tgl_lahir = models.DateField()
    masuk = models.IntegerField()
    lulus = models.IntegerField(null=True, blank=True)
    ppi = models.CharField(max_length=200)
    PA = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='SKPI/', null=True)
    prodi = models.CharField(max_length=90, choices=PRODI_CHOICES)

    def __str__(self):
        return self.nim

class organisasi(models.Model):
    nim = models.ForeignKey(data_skpi, on_delete=models.CASCADE)
    kegiatan = models.CharField(max_length=200)
    penempatan = models.CharField(max_length=50)
    periode = models.CharField(max_length=50)

    def __str__(self):
        return self.kegiatan

class pelatihan(models.Model):
    nim = models.ForeignKey(data_skpi, on_delete=models.CASCADE)
    pelatihan = models.CharField(max_length=200)
    pelaksana = models.CharField(max_length=50)
    periode = models.CharField(max_length=50)

    def __str__(self):
        return self.pelatihan

class penghargaan(models.Model):
    nim = models.ForeignKey(data_skpi, on_delete=models.CASCADE)
    penghargaan = models.CharField(max_length=200)
    prestasi = models.CharField(max_length=50)
    periode = models.CharField(max_length=50)

    def __str__(self):
        return self.penghargaan

class sertifikasi(models.Model):
    nim = models.ForeignKey(data_skpi, on_delete=models.CASCADE)
    bidang = models.CharField(max_length=200)
    no_sertifikat = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)

    def __str__(self):
        return self.bidang

class beasiswa(models.Model):
    nim = models.ForeignKey(data_skpi, on_delete=models.CASCADE)
    beasiswa = models.CharField(max_length=200)
    pemberi = models.CharField(max_length=50)
    periode = models.CharField(max_length=50)

    def __str__(self):
        return self.beasiswa



