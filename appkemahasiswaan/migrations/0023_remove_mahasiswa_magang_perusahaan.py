# Generated by Django 3.2.20 on 2023-10-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0022_perusahaan_ppi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahasiswa_magang',
            name='perusahaan',
        ),
    ]