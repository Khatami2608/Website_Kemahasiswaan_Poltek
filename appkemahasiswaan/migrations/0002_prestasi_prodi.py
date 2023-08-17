# Generated by Django 3.2.20 on 2023-07-30 10:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appkemahasiswaan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prestasi',
            fields=[
                ('id_prestasi', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=160)),
                ('prestasi', models.CharField(max_length=100)),
                ('penyelenggara', models.CharField(max_length=225)),
                ('tanggal', models.DateField()),
                ('tingkat', models.CharField(max_length=50)),
                ('juara', models.IntegerField()),
                ('gender', models.CharField(choices=[('laki-laki', 'Laki-Laki'), ('perempuan', 'Perempuan')], max_length=20)),
                ('publikasi', models.DateTimeField(auto_now_add=True)),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appkemahasiswaan.prodi')),
            ],
        ),
    ]