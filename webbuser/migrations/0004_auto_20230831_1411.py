# Generated by Django 3.2.20 on 2023-08-31 07:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0015_alter_artikel_deskripsi'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webbuser', '0003_profil_mhs_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilMahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmp_lahir', models.CharField(max_length=30)),
                ('tgl_lahir', models.DateField()),
                ('gender', models.CharField(choices=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], max_length=20)),
                ('Agama', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=150)),
                ('nomer_hp', models.CharField(max_length=15)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('foto', models.ImageField(null=True, upload_to='mahasiswa/')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='profil_mhs',
        ),
    ]
