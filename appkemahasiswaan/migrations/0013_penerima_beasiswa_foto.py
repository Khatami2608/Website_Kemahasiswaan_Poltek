# Generated by Django 3.2.20 on 2023-08-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0012_auto_20230828_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='foto',
            field=models.ImageField(null=True, upload_to='covers/penerima_beasiswa/'),
        ),
    ]