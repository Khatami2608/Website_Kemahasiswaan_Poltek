# Generated by Django 3.2.20 on 2023-08-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0010_auto_20230828_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='penerima_beasiswa',
            name='gender',
            field=models.CharField(choices=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], default='laki-laki', max_length=20),
        ),
    ]
