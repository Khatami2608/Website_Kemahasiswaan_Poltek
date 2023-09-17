# Generated by Django 3.2.20 on 2023-09-01 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webbuser', '0019_alter_data_skpi_prodi'),
    ]

    operations = [
        migrations.CreateModel(
            name='sertifikasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidang', models.CharField(max_length=200)),
                ('no_sertifikat', models.CharField(max_length=50)),
                ('penerbit', models.CharField(max_length=50)),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.data_skpi')),
            ],
        ),
        migrations.CreateModel(
            name='penghargaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penghargaan', models.CharField(max_length=200)),
                ('prestasi', models.CharField(max_length=50)),
                ('periode', models.CharField(max_length=50)),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.data_skpi')),
            ],
        ),
        migrations.CreateModel(
            name='pelatihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelatihan', models.CharField(max_length=200)),
                ('pelaksana', models.CharField(max_length=50)),
                ('periode', models.CharField(max_length=50)),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.data_skpi')),
            ],
        ),
        migrations.CreateModel(
            name='organisasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=200)),
                ('penempatan', models.CharField(max_length=50)),
                ('periode', models.CharField(max_length=50)),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.data_skpi')),
            ],
        ),
        migrations.CreateModel(
            name='beasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beasiswa', models.CharField(max_length=200)),
                ('pemberi', models.CharField(max_length=50)),
                ('periode', models.CharField(max_length=50)),
                ('nim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.data_skpi')),
            ],
        ),
    ]