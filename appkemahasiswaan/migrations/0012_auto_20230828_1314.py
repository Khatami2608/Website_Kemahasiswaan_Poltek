# Generated by Django 3.2.20 on 2023-08-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0011_penerima_beasiswa_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='smstr_akhir',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='smstr_awal',
            field=models.CharField(max_length=80, null=True),
        ),
    ]