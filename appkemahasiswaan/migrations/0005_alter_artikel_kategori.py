# Generated by Django 3.2.20 on 2023-08-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0004_anggota_organisasi_data_beasiswa_mahasiswa_magang_organisasi_penerima_beasiswa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='kategori',
            field=models.CharField(max_length=60),
        ),
    ]
