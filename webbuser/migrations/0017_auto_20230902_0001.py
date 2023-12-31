# Generated by Django 3.2.20 on 2023-09-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbuser', '0016_alter_data_skpi_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_skpi',
            name='foto',
            field=models.ImageField(null=True, upload_to='SKPI/'),
        ),
        migrations.AlterField(
            model_name='data_skpi',
            name='prodi',
            field=models.CharField(choices=[('Teknik Informasi', 'Teknik Informasi'), ('Teknik Mekatronika', 'Teknik Mekatronika'), ('Teknologi Elektronika', 'Teknologi Elektronika'), ('Akuntansi', 'Akuntansi'), ('Akuntansi Sektor Publik', 'Akuntansi Sektor Publik')], max_length=30),
        ),
    ]
