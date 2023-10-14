from django.shortcuts import render, redirect
from appkemahasiswaan.models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.views.generic import *
from django.core.paginator import Paginator 
from urllib.parse import urlencode
from django.shortcuts import get_object_or_404
from django.utils import timezone


def tambah_kategori(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tambah_artikel')  # Gantilah 'nama_url_yang_anda_inginkan' dengan URL yang sesuai.
    else:
        form = CategoryForm()
    return render(request, 'artikel/tambah_kategori.html', {'form': form})

def kategori(request):
    kategori = Category.objects.all()

    konteks = {
        'kategori': kategori,
    }
    return render(request, 'artikel/hapus_kategori.html', konteks)

def hapus_kategori(request, id_kategori):
    kategori = Category.objects.filter(id=id_kategori)
    kategori.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/hapus-kategori/')

def tambah_artikel(request):
    konteks = {}
    pesan = None  # Tambahkan ini di sini

    if request.method == 'POST':
        form = FormArtikel(request.POST, request.FILES)
        if form.is_valid():
            artikel = form.save(commit=False)
            action = request.POST.get('action')
            if action == 'draft':
                artikel.status = 'draft'
                pesan = "Data Berhasil Disimpan sebagai Draft"
            elif action == 'publish':
                artikel.status = 'published'
                artikel.published_date = timezone.now()
                pesan = "Data Berhasil Dipublikasikan"
            artikel.save()
            form = FormArtikel()
        else:
            pesan2 = "Lengkapi data yang ada"
            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
            return render(request, 'artikel/tambah_artikel.html', konteks)

    else:
        form = FormArtikel()

    konteks = {
        'form': form,
        'pesan': pesan,  # Sertakan pesan dalam konteks
    }
    
    return render(request, 'artikel/tambah_artikel.html', konteks)

def publish_artikel(request, artikel_id):
    artikel = get_object_or_404(Artikel, id=artikel_id)
    artikel.publish()
    return redirect('artikel:detail', slug=artikel.slug)

def draft_artikel(request, artikel_id):
    artikel = get_object_or_404(Artikel, id=artikel_id)
    artikel.unpublish()
    return redirect('artikel:detail', slug=artikel.slug)

def Tabel_ArtikelView(request):
    ordering = '-publikasi'

    tb_artikel = Artikel.objects.all().order_by(ordering)

    konteks = {
        'tb_artikel': tb_artikel,
    }

    return render(request, 'artikel/tabel_artikel.html', konteks)

def Edit_Artikel(request, id_Artikel):
    tb_artikel = Artikel.objects.get(id=id_Artikel)
    template = 'artikel/edit_artikel.html'
    if request.POST:
        form = FormArtikel(request.POST, request.FILES, instance=tb_artikel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('edit_artikel', id_Artikel=id_Artikel)
    else:
        form = FormArtikel(instance=tb_artikel)
        konteks = {
            'form': form,
            'tb_artikel': tb_artikel,
        }
    return render(request, template, konteks)

def Hapus_Artikel(request, id_Artikel):
    tb_artikel = Artikel.objects.filter(id=id_Artikel)
    tb_artikel.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/tabel-artikel/')

# START VIEW UNTUK PRESTASI
def PrestasiView(request):
    ordering = request.GET.get('ordering', '-nama')
    
    pretasi = Prestasi.objects.all().order_by(ordering)

    konteks = {
        'pretasi': pretasi,
        'ordering': ordering,
    }

    return render(request, 'prestasi/tabel-prestasi.html', konteks)
 

# Tambah Prestasi
def AddPrestasiView(request):
    form = FormPrestasi()
    pesan = ""

    if request.POST:
        form = FormPrestasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPrestasi()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'prestasi/tambah-prestasi.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    konteks = {
        'form': form,
        'pesan': pesan,
    }   
    return render(request, 'prestasi/tambah-prestasi.html', konteks)

def EditPrestasiView(request, nim_Prestasi):
    prestasi = Prestasi.objects.get(nim=nim_Prestasi)
    template = 'prestasi/Edit-prestasi.html'
    if request.POST:
        form = FormPrestasi(request.POST, request.FILES, instance=prestasi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_prestasi', nim_Prestasi=nim_Prestasi)
    else:
        form = FormPrestasi(instance=prestasi)
        konteks = {
            'form': form,
            'prestasi': prestasi,
        }
    return render(request, template, konteks)

# Proses Hapus data Kegiatan
def HapusPrstasiView(request, nim_Prestasi):
    prestasi = Prestasi.objects.filter(nim=nim_Prestasi)
    prestasi.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/prestasi/')

# END Prestasi
# Tambah data Pelanggaran
def AddPelanggaranView(request):
    form = FormPelanggaran()
    pesan = ""

    if request.POST:
        form = FormPelanggaran(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPelanggaran()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'pelanggaran/tambah-pelanggaran.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }


    konteks = {
        'form': form,
        'pesan': pesan,
    }
    
    return render(request, 'pelanggaran/tambah-pelanggaran.html', konteks)

# Tampilkan Data Pelanggaran
def PelanggaranView(request):
    ordering = '-publikasi'
    pelanggaran = Pelanggaran.objects.all().order_by(ordering)

    konteks = {
        'pelanggaran': pelanggaran,
        'ordering': ordering,
    }

    return render(request, 'pelanggaran/tabel-pelanggaran.html', konteks)

def EditPelanggaranView(request, nim_pelanggaran):
    pelanggaran = get_object_or_404(Pelanggaran, nim=nim_pelanggaran)
    form = FormPelanggaran(instance=pelanggaran)
    pesan = ""

    if request.method == 'POST':
        form = FormPelanggaran(request.POST, instance=pelanggaran)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diubah"
            return redirect('/pelanggaran/')  # Anda dapat menggantinya dengan URL yang sesuai

    konteks = {
        'form': form,
        'pesan': pesan,
    }

    return render(request, 'pelanggaran/edit-pelanggaran.html', konteks)

def HapusPelanggaranView(request, nim_pelanggaran):
    pelanggaran = Pelanggaran.objects.filter(nim=nim_pelanggaran)
    pelanggaran.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/pelanggaran/')

# START DATA BEASISWA
def AddDataBeasiswa(request):
    form = FormDataBeasiswa()
    pesan = ""

    if request.POST:
        form = FormDataBeasiswa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormDataBeasiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Data_Beasiswa/AddData_Beasiswa.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    else:
        form = FormDataBeasiswa()

    konteks = {
        'form': form,
    }
    return render(request, 'Data_Beasiswa/AddData_Beasiswa.html', konteks)

def DataBeasiswa(request):
    nama = request.GET.get('carinama')
    ordering = '-publikasi'
    
    data_beasiswa = Data_Beasiswa.objects.all().order_by(ordering)

    if nama:
        data_beasiswa = data_beasiswa.filter(nama__icontains=nama)

    paginator = Paginator(data_beasiswa, 10)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    data_beasiswa = paginator.get_page(page_number)

    konteks = {
        'data_beasiswa': data_beasiswa,
        'nama': nama,
        'ordering': ordering,
    }
    return render(request, 'Data_Beasiswa/data-beasiswa.html', konteks)

def Ubah_DataBeasiswa(request, Data_Beasiswa_nama):
    data_beasiswa = Data_Beasiswa.objects.get(nama=Data_Beasiswa_nama)
    template = 'Data_Beasiswa/Ubah-DataBeasiwa.html'
    if request.POST:
        form = FormDataBeasiswa(request.POST, request.FILES, instance=data_beasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Ubah_Data_Beasiswa', Data_Beasiswa_nama=Data_Beasiswa_nama)
    else:
        form = FormDataBeasiswa(instance=data_beasiswa)
        konteks = {
            'form': form,
            'data_beasiswa': data_beasiswa,
        }
    return render(request, template, konteks)

def Hapus_DataBeasiswa(request, Data_Beasiswa_nama):
    data_beasiswa = Data_Beasiswa.objects.filter(nama=Data_Beasiswa_nama)
    data_beasiswa.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/Data-Beasiswa/')

def Tambah_Penerima(request):
    form_penerima = FormPenerima_Beasiswa()
    pesan = ""

    if request.method == 'POST':
        form_penerima = FormPenerima_Beasiswa(request.POST, request.FILES)
        if form_penerima.is_valid():
            penerima = form_penerima.save()  # Save penerima data
            return redirect('tambah_beasiswa', nim_penerima=penerima.nim)

        pesan = "Lengkapi data yang ada"

    konteks = {
        'form_penerima': form_penerima,
        'pesan': pesan,
    }
    return render(request, 'Penerima_Beasiswa/tambah-penerima.html', konteks)

def Tambah_Beasiswa(request, nim_penerima):
    penerima = Penerima_Beasiswa.objects.get(nim=nim_penerima)
    form_beasiswa = FormBeasiswa()
    pesan = ""

    if request.method == 'POST':
        form_beasiswa = FormBeasiswa(request.POST)
        if form_beasiswa.is_valid():
            beasiswa = form_beasiswa.save(commit=False)
            beasiswa.id_beasiswa = penerima
            beasiswa.save()
            pesan = "Data Berhasil Disimpan"
        else:
            pesan = "Lengkapi data yang ada"

    konteks = {
        'form_beasiswa': form_beasiswa,
        'pesan': pesan,
        'penerima': penerima,
    }
    return render(request, 'Penerima_Beasiswa/tambah-beasiswa.html', konteks)


def Penerima_BeasiswaView(request):
    nama = request.GET.get('cari')
    prodi = request.GET.get('cariprodi')
    ordering = '-publikasi'
    form = FormPenerima_Beasiswa()
    
    penerima = Penerima_Beasiswa.objects.all().order_by(ordering)
    beasiswa = Beasiswa.objects.filter(id_beasiswa=penerima)

    if nama:
        penerima = penerima.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama) | Q(angkatan__icontains=nama)
        )

    if prodi:
        penerima = penerima.filter(prodi=prodi)

    paginator = Paginator(penerima, 10)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    penerima = paginator.get_page(page_number)

    konteks = {
        'penerima': penerima,
        'beasiswa': beasiswa,
        'prodi': prodi,
        'form': form,
        'nama': nama,
        'ordering': ordering,
    }
    return render(request, 'Penerima_Beasiswa/penerima-beasiswa.html', konteks)

def edit_penerima(request, nim_penerima):
    penerima = Penerima_Beasiswa.objects.get(nim=nim_penerima)
    template = 'Penerima_Beasiswa/edit-penerima-beasiswa.html'
    if request.method == 'POST':
        form = FormPenerima_Beasiswa(request.POST, request.FILES, instance=penerima)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('edit_penerima', nim_penerima=nim_penerima)
    else:
        form = FormPenerima_Beasiswa(instance=penerima)

    konteks = {
        'form': form,
        'penerima': penerima,
    }
    return render(request, template, konteks)
 
def edit_beasiswa(request, id_beasiswa):
    beasiswa = get_object_or_404(Beasiswa, id_beasiswa=id_beasiswa)
    if request.method == 'POST':
        form = FormBeasiswa(request.POST, instance=beasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Beasiswa Berhasil Diperbaharui!')
            return redirect('edit_beasiswa', id_beasiswa=id_beasiswa)
    else:
        form = FormBeasiswa(instance=beasiswa)

    konteks = {
        'form': form,
        'beasiswa': beasiswa,
    }
    return render(request, 'Penerima_Beasiswa/edit-beasiswa.html', konteks)

def Hapus_Penerima_Beasiswa(request, nim_Penerima_Beasiswa):
    penerima = Penerima_Beasiswa.objects.filter(nim=nim_Penerima_Beasiswa)
    penerima.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/penerima-beasiswa/')

def DetailPenerima(request, nim_Penerima_Beasiswa):
    detail = get_object_or_404(Penerima_Beasiswa, nim=nim_Penerima_Beasiswa)
    detail2 = Beasiswa.objects.filter(id_beasiswa=detail)
    template = 'Penerima_Beasiswa/detail_penerima.html'
    
    pesan = ""

    if request.method == 'POST':
        form_beasiswa = FormBeasiswa(request.POST)
        if form_beasiswa.is_valid():
            beasiswa = form_beasiswa.save(commit=False)
            beasiswa.id_beasiswa = detail  # Set the foreign key to the Penerima_Beasiswa instance
            beasiswa.save()
            pesan = "Data Berhasil Disimpan"
        else:
            pesan = "Lengkapi data yang ada"

    form_beasiswa = FormBeasiswa()  # Create a new instance of the form for rendering
    konteks = {
        'form_beasiswa': form_beasiswa,
        'pesan': pesan,
        'detail': detail,
        'detail2': detail2,
    }
    return render(request, template, konteks)


# Praktek Magang
def Tambah_Mhs_Magang(request):
    form = FormMahasiswa_Magang()
    pesan = ""

    if request.POST:
        form = FormMahasiswa_Magang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormMahasiswa_Magang()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Magang/tambah_mahasiswa_magang.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    konteks = {
        'form': form,
        'pesan': pesan,
    }   
    return render(request, 'Magang/tambah_mahasiswa_magang.html', konteks)

def Mahasiswa_MagangView(request):
    nama = request.GET.get('cari')
    prodi = request.GET.get('prodi')
    semester = request.GET.get('smtr')
    ordering = '-publikasi'
    form = FormMahasiswa_Magang()
    
    magang = Mahasiswa_Magang.objects.all().order_by(ordering)

    if nama:
        magang = magang.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama) | Q(angkatan__icontains=nama)
        )

    if prodi:
        magang = magang.filter(prodi=prodi)

    if semester:
        magang = magang.filter(semester=semester)

    paginator = Paginator(magang, 10) 
    page_number = request.GET.get('page')
    magang = paginator.get_page(page_number)

    konteks = {
        'magang': magang,
        'prodi': prodi,
        'semester': semester,
        'form': form,
        'nama': nama,
        'ordering': ordering,
    }
    return render(request, 'Magang/mahasiswa_ppi.html', konteks)

def Edit_MagangView(request, nim_Mahasiswa_Magang):
    Magang = Mahasiswa_Magang.objects.get(nim=nim_Mahasiswa_Magang)
    template = 'Magang/edit_mahasiswa_ppi.html'
    if request.method == 'POST':
        form = FormMahasiswa_Magang(request.POST, request.FILES, instance=Magang)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_Mahasiswa_PPI', nim_Mahasiswa_Magang=nim_Mahasiswa_Magang)
    else:
        form = FormMahasiswa_Magang(instance=Magang)
    konteks = {
        'form': form,
        'Magang': Magang,
    }
    return render(request, template, konteks)

def Hapus_Magang(request, nim_Mahasiswa_Magang):
    magang = Mahasiswa_Magang.objects.filter(nim=nim_Mahasiswa_Magang)
    magang.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/mahasiswa-ppi/')

def OrganisasiView(request):
    ordering = '-publikasi'
    cari = request.GET.get('cari')
    form = Form_Organisasi()
    organisasi = Organisasi.objects.all().order_by(ordering)

    if cari:
        organisasi = organisasi.filter(organisasi__icontains=cari)

    paginator = Paginator(organisasi, 10) 
    page_number = request.GET.get('page')
    organisasi = paginator.get_page(page_number)

    konteks = {
        'cari': cari,
        'organisasi': organisasi,
        'form': form,
        'ordering': ordering,
    }
    return render(request, 'Organisasi/organisasi.html', konteks)

def Tambah_Organisasi(request):
    form = Form_Organisasi()
    pesan = ""

    if request.POST:
        form = Form_Organisasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Form_Organisasi()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Organisasi/tambah_organisasi.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    konteks = {
        'form': form,
        'pesan': pesan,
    }   
    return render(request, 'Organisasi/tambah_organisasi.html', konteks)

def Edit_Organisasi(request, id_organisasi_Organisasi):
    organisasi = Organisasi.objects.get(id_organisasi=id_organisasi_Organisasi)
    template = 'Organisasi/edit-organisasi.html'
    if request.method == 'POST':
        form = Form_Organisasi(request.POST, request.FILES, instance=organisasi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_Organisasi', id_organisasi_Organisasi=id_organisasi_Organisasi)
    else:
        form = Form_Organisasi(instance=organisasi)
    konteks = {
        'form': form,
        'organisasi': organisasi,
    }
    return render(request, template, konteks)

def Hapus_Organisasi(request, id_organisasi_Organisasi):
    organisasi = Organisasi.objects.filter(id_organisasi=id_organisasi_Organisasi)
    organisasi.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/organisasi/')

def Tambah_Anggota(request):
    form = Form_Anggota_Organisasi()
    pesan = ""

    if request.POST:
        form = Form_Anggota_Organisasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Form_Anggota_Organisasi()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Anggota_Organisasi/tambah_anggota.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    konteks = {
        'form': form,
        'pesan': pesan,
    }   
    return render(request, 'Anggota_Organisasi/tambah_anggota.html', konteks)

def AnggotaView(request):
    ordering = '-publikasi'
    anggota = Anggota_Organisasi.objects.all().order_by(ordering)

    konteks = {
        'anggota': anggota,
        'ordering': ordering,
    }
    return render(request, 'Anggota_Organisasi/data_anggota.html', konteks)

def Edit_AnggotaView(request, id_anggota_Anggota_Organisasi):
    anggota = Anggota_Organisasi.objects.get(id_anggota=id_anggota_Anggota_Organisasi)
    template = 'Anggota_Organisasi/edit-anggota.html'
    if request.method == 'POST':
        form = Form_Anggota_Organisasi(request.POST, request.FILES, instance=anggota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_Anggota', id_anggota_Anggota_Organisasi=id_anggota_Anggota_Organisasi)
    else:
        form = Form_Anggota_Organisasi(instance=anggota)
    konteks = {
        'form': form,
        'anggota': anggota,
    }
    return render(request, template, konteks)

def Hapus_AnggotaView(request, id_anggota_Anggota_Organisasi):
    anggota = Anggota_Organisasi.objects.filter(id_anggota=id_anggota_Anggota_Organisasi)
    anggota.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/data-anggota/')

def tambah_user():
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user.set_password(password)  # Setel kata sandi pengguna
            user.save()  # Simpan pengguna ke database
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Data berhasil disimpan.')
                return redirect('dashboard')
        else:
            messages.error(request, 'Periksa Kembali !!.')
    else:
        form = UserRegistrationForm()
    return render(request, 'User/tambah_user.html', {'form': form})

def UserView(request):
    userview = User.objects.all()

    konteks = {
        'userview': userview,
    }
    return render(request, 'User/data_user.html', konteks)

def Tambah_Prodi(request):
    form = FormProdi()
    pesan = ""

    if request.POST:
        form = FormProdi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormProdi()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Prodi/tambah_prodi.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }
    konteks = {
        'form': form,
        'pesan': pesan,
    }   
    return render(request, 'Prodi/tambah_prodi.html', konteks)

def ProdiViews(request):
    prodi = Prodi.objects.all()

    konteks = {
        'prodi': prodi,
    }
    return render(request, 'Prodi/tabel_prodi.html', konteks)

def Edit_Prodi(request, id_Prodi):
    prodi = Prodi.objects.get(id=id_Prodi)
    template = 'Prodi/edit_prodi.html'
    if request.method == 'POST':
        form = FormProdi(request.POST, request.FILES, instance=prodi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_Prodi', id_Prodi=id_Prodi)
    else:
        form = FormProdi(instance=prodi)
    konteks = {
        'form': form,
        'prodi': prodi,
    }
    return render(request, template, konteks)

def Hapus_Prodi(request, id_Prodi):
    prodi = Prodi.objects.filter(id=id_Prodi)
    prodi.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/tabel-prodi/')