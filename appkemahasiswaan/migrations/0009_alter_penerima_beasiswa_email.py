# Generated by Django 3.2.20 on 2023-08-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0008_auto_20230828_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penerima_beasiswa',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
