from django.db import models

class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )  

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, default=None) 
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
