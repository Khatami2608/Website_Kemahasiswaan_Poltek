# Generated by Django 3.2.20 on 2023-09-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbuser', '0017_auto_20230902_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_skpi',
            name='gender',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=30),
        ),
        migrations.AlterField(
            model_name='data_skpi',
            name='prodi',
            field=models.CharField(choices=[('Teknik Informasi', 'TI'), ('Teknik Mekatronika', 'TM'), ('Teknologi Elektronika', 'TE'), ('Akuntansi', 'AK'), ('Akuntansi Sektor Publik', 'ASP')], max_length=60),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=30),
        ),
    ]
