# Generated by Django 3.2.20 on 2023-08-31 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbuser', '0002_profil_mhs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil_mhs',
            name='foto',
            field=models.ImageField(null=True, upload_to='mahasiswa/'),
        ),
    ]
