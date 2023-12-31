# Generated by Django 3.2.20 on 2023-08-31 04:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_mahasiswa'),
        ('appkemahasiswaan', '0015_alter_artikel_deskripsi'),
        ('webbuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profil_mhs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tmp_lahir', models.CharField(max_length=30)),
                ('tgl_lahir', models.DateField()),
                ('gender', models.CharField(choices=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], max_length=20)),
                ('Agama', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=150)),
                ('nomer_hp', models.CharField(max_length=15)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
                ('user_mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_mahasiswa')),
            ],
        ),
    ]
