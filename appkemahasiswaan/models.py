from django.db import models
from PIL import Image
from django.utils.text import slugify
import uuid

class Category(models.Model):
	kategori = models.CharField(max_length=60)

	def __str__(self):
	 	return self.kategori 

class Artikel(models.Model):
	judul = models.CharField(max_length=225)
	Deskripsi = models.TextField()
	kategori = models.CharField(max_length=60)
	image = models.ImageField(upload_to='covers/', null=True)
	publikasi = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('kegiatan:detail', kwargs = url_slug)

	def __str__(self):
	 	return self.judul 

class Prodi(models.Model):
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return self.prodi

GENDER_CHOICES = [
    ('laki-laki', 'Laki-Laki'),
    ('perempuan', 'Perempuan'),
]

SEMESTER_CHOICES = [
    ('ganjil', 'Ganjil'),
    ('genap', 'Genap'),
]

class Prestasi(models.Model):
    id_prestasi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nim = models.IntegerField()
    nama = models.CharField(max_length=160)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    prestasi = models.CharField(max_length=100)
    penyelenggara = models.CharField(max_length=225)
    tanggal = models.DateField()
    tingkat = models.CharField(max_length=50)
    juara = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    publikasi = models.DateTimeField(auto_now_add=True)

class Pelanggaran(models.Model):
    id_pelanggaran = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nim = models.IntegerField()
    nama = models.CharField(max_length=100)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES) 
    angkatan = models.IntegerField()
    Jenis_pelanggaran = models.CharField(max_length=300)
    sanksi = models.CharField(max_length=300)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nim)

class Data_Beasiswa(models.Model):
    id_beasiswa = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=100)
    dibuka = models.DateField()
    ditutup = models.DateField()
    benefit = models.TextField()
    deskripsi = models.TextField()
    persyaratan = models.TextField()
    ip_minimal = models.IntegerField()
    ipk_minimal = models.IntegerField()
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='covers/', null=True)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Penerima_Beasiswa(models.Model):
    nim = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100)
    angkatan = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    email = models.CharField(max_length=100) 
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    beasiswa = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nim)

class Mahasiswa_Magang(models.Model):
    nim = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=200)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    angkatan = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    jalur_masuk = models.CharField(max_length=100)
    tgl_magang = models.DateField()
    perusahaan = models.CharField(max_length=300)
    pembimbing = models.CharField(max_length=200)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nim)

STATUS_CHOICES = [
    ('Aktif', 'Aktif'),
    ('Tidak Aktif', 'Tidak Aktif'),
]

class Organisasi(models.Model):
    id_organisasi = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organisasi = models.CharField(max_length=100)
    visi = models.TextField()
    misi = models.TextField()
    logo = models.ImageField(upload_to='organisasi/', null=True)
    publikasi = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aktif')

    def __str__(self):
        return str(self.organisasi)

class Anggota_Organisasi(models.Model):
    id_anggota = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nim = models.IntegerField()
    nama = models.CharField(max_length=100)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    angkatan =  models.IntegerField()
    organisasi = models.ForeignKey(Organisasi, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='organisasi/anggota/', null=True)
    publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nim)