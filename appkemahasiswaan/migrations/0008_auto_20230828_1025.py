# Generated by Django 3.2.20 on 2023-08-28 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0007_alter_organisasi_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='smtr_akhir',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='smtr_awal',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
