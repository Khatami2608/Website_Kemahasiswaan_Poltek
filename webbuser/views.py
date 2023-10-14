from django.shortcuts import render, redirect
from django.views.generic import *
from appkemahasiswaan.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from urllib.parse import urlencode
from .models import *
from login.models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import FileResponse
from xhtml2pdf import pisa
from io import BytesIO
from .forms import *
from django.contrib import messages
# diango login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from login.models import user_mahasiswa
from django.contrib.auth.decorators import login_required

# membuat login
def home(request):
    ordering = '-publikasi'
    tb_artikel = Artikel.objects.all().order_by(ordering)

    paginator = Paginator(tb_artikel, 3)
    page_number = request.GET.get('page')
    tb_artikel_page = paginator.get_page(page_number)

    konteks = {
        'tb_artikel': tb_artikel_page,
    }
    return render(request, 'home/home.html')

def ArtikelList(request):
    ordering = '-publikasi'
    tb_artikel = Artikel.objects.filter(status='published').order_by(ordering)
    kategori = Artikel.objects.all()
    search = request.GET.get('cari')
    cari_tgl = request.GET.get('tanggal')

    if search:
        tb_artikel = tb_artikel.filter(
            Q(judul__icontains=search) | Q(kategori__icontains=search)
        )
    if cari_tgl:
        tb_artikel = tb_artikel.filter(publikasi__date=cari_tgl)

    paginator = Paginator(tb_artikel, 4)
    page_number = request.GET.get('page')
    tb_artikel_page = paginator.get_page(page_number)

    konteks = {
        'tb_artikel': tb_artikel_page,
        'kategori': kategori,
    }
    return render(request, 'artikel_user/artikel.html', konteks)

def ArtikelDetail(request, slug_Artikel):
    artikel = Artikel.objects.get(slug=slug_Artikel)
    template = "artikel_user/artikel_detail.html"
    kategori = Artikel.objects.all()

    konteks = {
        'artikel': artikel,
        'kategori': kategori,
    }
    return render(request, template, konteks)

def ArtikelKategoriList(request, kategori_Artikel):
    ordering = '-publikasi'
    tb_artikel = Artikel.objects.filter(kategori__icontains=kategori_Artikel).order_by(ordering)
    kategori = Artikel.objects.all()

    paginator = Paginator(tb_artikel, 5)
    page_number = request.GET.get('page')
    tb_artikel_page = paginator.get_page(page_number)

    konteks = {
        'tb_artikel': tb_artikel,
        'kategori': kategori,
    }
    return render(request, 'artikel_user/kategori.html', konteks)

def ListBeasiswa(request):
    ordering = '-publikasi'
    
    data_beasiswa = Data_Beasiswa.objects.all().order_by(ordering)

    paginator = Paginator(data_beasiswa, 10)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    data_beasiswa = paginator.get_page(page_number)

    konteks = {
        'data_beasiswa': data_beasiswa,
        'ordering': ordering,
    }
    return render(request, 'Beasiswa/List_beasiswa.html', konteks)

def OrganisasiList(request):
    organisasi = Organisasi.objects.all()

    konteks = {
        'organisasi': organisasi,
    }
    return render(request, 'organisasi_user/organisasi_list.html', konteks)


# Eksport CV Ke PDF
def export_cv_to_pdf(request):
    personal_info = PersonalInfo.objects.first()
    pendidikan_list = Pendidikan.objects.filter(personal_info=personal_info)
    skill_list = Skill.objects.filter(personal_info=personal_info)
    training_list = Training.objects.filter(personal_info=personal_info)

    context = {
        'personal_info': personal_info,
        'pendidikan_list': pendidikan_list,
        'skill_list': skill_list,
        'training_list': training_list,
        'exporting_pdf': True,
    }

    template = get_template('curriculum_vitae/personal_cv2.html')
    html_content = template.render(context)

    pdf_buffer = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_buffer)

    if not pdf.err:
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="CV.pdf"'
        return response
    return HttpResponse('Error saat menghasilkan PDF', content_type='text/plain')

# Tambah Data CV
def tambah_data(request):
    personal_info_form = PersonalInfoForm()
    pendidikan_form = PendidikanForm()
    skill_form = SkillForm()
    training_form = TrainingForm()

    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST, request.FILES)
        pendidikan_form = PendidikanForm(request.POST)
        skill_form = SkillForm(request.POST)
        training_form = TrainingForm(request.POST)

        if (
            personal_info_form.is_valid() and 
            pendidikan_form.is_valid() and 
            skill_form.is_valid() and 
            training_form.is_valid()
        ):
            personal_info = personal_info_form.save()
            pendidikan = pendidikan_form.save(commit=False)
            pendidikan.personal_info = personal_info
            pendidikan.save()

            skill = skill_form.save(commit=False)
            skill.personal_info = personal_info
            skill.save()

            training = training_form.save(commit=False)
            training.personal_info = personal_info
            training.save()

            return redirect('detail_personal_info', personal_info_id=personal_info.id)  # Pastikan URL dan nama view sesuai

    context = {
        'personal_info_form': personal_info_form,
        'pendidikan_form': pendidikan_form,
        'skill_form': skill_form,
        'training_form': training_form,
    }

    return render(request, 'curriculum_vitae/index1.html', context)

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profil')
    else:
        form = ProfilForm()
    return render(request, 'profil_mhs/create_profile.html', {'form': form})

@login_required
def profile(request):
    profil = ProfilMahasiswa.objects.get(user=request.user)
    return render(request, 'profil_mhs/profil2.html', {'profil': profil})

# Curriculum Vitae

def input_personal_info(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            personal_info = form.save()
            return redirect('input_pendidikan', personal_info_id=personal_info.id)
    else:
        form = PersonalInfoForm()
    return render(request, 'curriculum_vitae/input_personal_info.html', {'form': form})

def input_pendidikan(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    if request.method == 'POST':
        form = PendidikanForm(request.POST)
        if form.is_valid():
            pendidikan = form.save(commit=False)
            pendidikan.personal_info = personal_info
            pendidikan.save()
            return redirect('input_skill', personal_info_id=personal_info.id)
    else:
        form = PendidikanForm()
    return render(request, 'curriculum_vitae/input_pendidikan.html', {'form': form, 'personal_info': personal_info})

def input_skill(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.personal_info = personal_info
            skill.save()
            return redirect('input_training', personal_info_id=personal_info.id)
    else:
        form = SkillForm()
    return render(request, 'curriculum_vitae/input_skill.html', {'form': form, 'personal_info': personal_info})

def input_training(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    if request.method == 'POST':
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.personal_info = personal_info
            training.save()
            return redirect('personal_cv', personal_info_id=personal_info.id)
    else:
        form = TrainingForm()
    return render(request, 'curriculum_vitae/input_training.html', {'form': form, 'personal_info': personal_info})

def personal_cv(request, personal_info_id):
    personal_info = PersonalInfo.objects.get(id=personal_info_id)
    pendidikan_list = Pendidikan.objects.filter(personal_info=personal_info)
    skill_list = Skill.objects.filter(personal_info=personal_info)
    training_list = Training.objects.filter(personal_info=personal_info)
    
    context = {
        'personal_info': personal_info,
        'pendidikan_list': pendidikan_list,
        'skill_list': skill_list,
        'training_list': training_list,
    }
    return render(request, 'curriculum_vitae/personal_cv2.html', context)

def Addskpi_Personal(request):
    pesan = ""

    if request.method == 'POST': 
        form_skpi = SkpiForm(request.POST, request.FILES)
        if form_skpi.is_valid():
            skpi_instance = form_skpi.save(commit=False)  # Tidak langsung menyimpan ke database
            if 'foto' in request.FILES:
                skpi_instance.foto = request.FILES['foto']  # Mengisi bidang 'foto' dengan file yang diunggah
            skpi_instance.save()  # Simpan data ke database
            pesan = "Data Berhasil Disimpan"
            form_skpi = SkpiForm()  # Setelah berhasil, reset formulir
        else:
            pesan = "Lengkapi data yang ada"
    else:
        form_skpi = SkpiForm()  # Jika bukan metode POST, inisialisasi formulir

    konteks = {
        'form_skpi': form_skpi,
        'pesan': pesan,
    }
    return render(request, 'SKPI/tambah_skpi.html', konteks)

def ViewSKPI(request, data_skpi_nim):
    skpi = data_skpi.objects.get(nim=data_skpi_nim)
    Organisasi = organisasi.objects.filter(nim=skpi)
    Pelatihan = pelatihan.objects.filter(nim=skpi)
    Penghargaan = penghargaan.objects.filter(nim=skpi)
    Sertifikasi = sertifikasi.objects.filter(nim=skpi)
    Beasiswa = beasiswa.objects.filter(nim=skpi)

    konteks = {
        'skpi': skpi,
        'Organisasi': Organisasi,
        'Pelatihan': Pelatihan,
        'Penghargaan': Penghargaan,
        'Sertifikasi': Sertifikasi,
        'Beasiswa': Beasiswa,
    }
    return render(request, 'SKPI/data_skpi.html', konteks)

def Edit_skpi(request, data_skpi_nim):
    skpi = data_skpi.objects.get(nim=data_skpi_nim)
    template = 'SKPI/edit-skpi.html'
    if request.method == 'POST':
        form = SkpiForm(request.POST, request.FILES, instance=skpi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_data_skpi', data_skpi_nim=data_skpi_nim)
    else:
        form = SkpiForm(instance=skpi)
    konteks = {
        'form': form,
        'skpi': skpi,
    }
    return render(request, template, konteks)

def tambah_organisasi(request, data_skpi_nim):
    mahasiswa = data_skpi.objects.get(nim=data_skpi_nim)

    if request.method == 'POST':
        form = OrganisasiForm(request.POST)
        if form.is_valid():
            organisasi = form.save(commit=False)
            organisasi.nim = mahasiswa
            organisasi.save()
            messages.success(request, 'Data Organisasi Berhasil Disimpan')  # Menambahkan pesan berhasil
            return redirect('tambah_organisasi', data_skpi_nim=data_skpi_nim)
        else:
            messages.error(request, 'Data Organisasi Gagal Disimpan. Pastikan semua kolom terisi dengan benar.')  # Menambahkan pesan gagal jika form tidak valid
    else:
        form = OrganisasiForm()

    konteks = {
        'form': form,
        'mahasiswa': mahasiswa,
    }
    return render(request, 'SKPI/tambah-organisasi.html', konteks)

def tambah_pelatihan(request, data_skpi_nim):
    pelatihan1 = data_skpi.objects.get(nim=data_skpi_nim)

    if request.method == 'POST':
        form = PelatihanForm(request.POST)
        if form.is_valid():
            pelatihan = form.save(commit=False)
            pelatihan.nim = pelatihan1
            pelatihan.save()
            messages.success(request, 'Data Pelatihan Berhasil Disimpan')  # Menambahkan pesan berhasil
            return redirect('pelatihan', data_skpi_nim=data_skpi_nim)
        else:
            messages.error(request, 'Data Pelatihan Gagal Disimpan. Pastikan semua kolom terisi dengan benar.')  # Menambahkan pesan gagal jika form tidak valid
    else:
        form = PelatihanForm()

    konteks = {
        'form': form,
        'pelatihan1': pelatihan1,
    }
    return render(request, 'SKPI/tambah-pelatihan.html', konteks)

def tambah_penghargaan(request, data_skpi_nim):
    dt_penghargaan = data_skpi.objects.get(nim=data_skpi_nim)

    if request.method == 'POST':
        form = PenghargaanForm(request.POST)
        if form.is_valid():
            penghargaan = form.save(commit=False)
            penghargaan.nim = dt_penghargaan
            penghargaan.save()
            messages.success(request, 'Data Penghargaan Berhasil Disimpan')  # Menambahkan pesan berhasil
            return redirect('penghargaan', data_skpi_nim=data_skpi_nim)
        else:
            messages.error(request, 'Data Penghargaan Gagal Disimpan. Pastikan semua kolom terisi dengan benar.')  # Menambahkan pesan gagal jika form tidak valid
    else:
        form = PenghargaanForm()

    konteks = {
        'form': form,
        'dt_penghargaan': dt_penghargaan,
    }
    return render(request, 'SKPI/tambah_penghargaan.html', konteks)

def tambah_sertifikasi(request, data_skpi_nim):
    dt_sertifikasi = data_skpi.objects.get(nim=data_skpi_nim)

    if request.method == 'POST':
        form = SertifikasiForm(request.POST)
        if form.is_valid():
            sertifikasi = form.save(commit=False)
            sertifikasi.nim = dt_sertifikasi
            sertifikasi.save()
            messages.success(request, 'Data Sertifikasi Berhasil Disimpan')  # Menambahkan pesan berhasil
            return redirect('sertifikasi', data_skpi_nim=data_skpi_nim)
        else:
            messages.error(request, 'Data Sertifikasi Gagal Disimpan. Pastikan semua kolom terisi dengan benar.')  # Menambahkan pesan gagal jika form tidak valid
    else:
        form = SertifikasiForm()

    konteks = {
        'form': form,
        'dt_sertifikasi': dt_sertifikasi,
    }
    return render(request, 'SKPI/tambah_sertifikasi.html', konteks)

def tambah_beasiswa(request, data_skpi_nim):
    dt_beasiswa = data_skpi.objects.get(nim=data_skpi_nim)

    if request.method == 'POST':
        form = BeasiswaForm(request.POST)
        if form.is_valid():
            beasiswa = form.save(commit=False)
            beasiswa.nim = dt_beasiswa
            beasiswa.save()
            messages.success(request, 'Data Beasiswa Berhasil Disimpan')  # Menambahkan pesan berhasil
            return redirect('tb_beasiswa', data_skpi_nim=data_skpi_nim)
        else:
            messages.error(request, 'Data Beasiswa Gagal Disimpan. Pastikan semua kolom terisi dengan benar.')  # Menambahkan pesan gagal jika form tidak valid
    else:
        form = BeasiswaForm()

    konteks = {
        'form': form,
        'dt_beasiswa': dt_beasiswa,
    }
    return render(request, 'SKPI/tambahdata_beasiswa.html', konteks)

def tes_template(request):
    return render(request, 'test_template.html')
