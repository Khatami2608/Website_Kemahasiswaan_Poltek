# Generated by Django 3.2.20 on 2023-08-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('tgl_lahir', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('warga_negara', models.CharField(max_length=50)),
                ('agama', models.CharField(max_length=50)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('nomer_hp', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='foto_cv/')),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.CharField(max_length=150)),
                ('tahun', models.PositiveIntegerField()),
                ('penyelenggara', models.CharField(max_length=100)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidang', models.CharField(max_length=50)),
                ('keterangan', models.CharField(max_length=50)),
                ('personal_info', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webbuser.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pendidikan', models.CharField(max_length=100)),
                ('masuk', models.PositiveIntegerField()),
                ('tamat', models.PositiveIntegerField()),
                ('jenjang', models.CharField(max_length=100)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webbuser.personalinfo')),
            ],
        ),
    ]
