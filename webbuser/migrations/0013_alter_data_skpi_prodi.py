# Generated by Django 3.2.20 on 2023-09-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbuser', '0012_data_skpi_prodi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_skpi',
            name='prodi',
            field=models.CharField(choices=[('TI', 'Teknik Informasi'), ('TM', 'Teknik Mekatronika'), ('TE', 'Teknologi Elektronika'), ('AK', 'Akuntansi'), ('ASP', 'Akuntansi Sektor Publik')], max_length=3),
        ),
    ]
