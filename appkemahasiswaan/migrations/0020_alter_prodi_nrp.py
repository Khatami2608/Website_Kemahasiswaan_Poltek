# Generated by Django 3.2.20 on 2023-10-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0019_auto_20230912_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodi',
            name='nrp',
            field=models.IntegerField(),
        ),
    ]
