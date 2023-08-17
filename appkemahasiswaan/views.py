from django.shortcuts import render, redirect
from appkemahasiswaan.models import *
from .forms import *
from django.contrib import messages
from django.views.generic import *
from django.core.paginator import Paginator 
from urllib.parse import urlencode

# Tambah Artikel
def tambah_artikel(request):
    konteks = {}

    if request.POST:
        form = FormArtikel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormArtikel()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'artikel/tambah_artikel.html', konteks)
        else:
            pesan2 = "Lengkapi data yang ada"

            konteks = {
                'form': form,
                'pesan2': pesan2,
            }

    else:
        form = FormArtikel()

        konteks = {
            'form': form,
        }    
    return render(request, 'artikel/tambah_artikel.html', konteks)

def Tabel_ArtikelView(request):
    ordering = '-publikasi'
    keyword = request.GET.get('cari')  # Use GET instead of POST for search keyword
    cari_tgl = request.GET.get('cari_tgl')  # Change to 'cari_tgl'

    tb_artikel = Artikel.objects.all()

    if keyword:
        tb_artikel = tb_artikel.filter(judul__icontains=keyword)

    # Filter berdasarkan tanggal_publikasi
    if cari_tgl:
        tb_artikel = tb_artikel.filter(publikasi__date=cari_tgl)

    # Ordering
    tb_artikel = tb_artikel.order_by(ordering)

    # Pagination
    paginator = Paginator(tb_artikel, 2) 
    page_number = request.GET.get('page')
    tb_artikel = paginator.get_page(page_number)

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
    nama = request.GET.get('carinama')
    ordering = request.GET.get('ordering', '-nama')
    form = FormPrestasi()
    prodi = request.GET.get('cariprodi')
    
    pretasi = Prestasi.objects.all()

    if nama:
        pretasi = pretasi.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama)
        )

    if prodi:
        pretasi = pretasi.filter(prodi=prodi)

    pretasi = pretasi.order_by(ordering)

    paginator = Paginator(pretasi, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    pretasi = paginator.get_page(page_number)

    konteks = {
        'form': form,
        'pretasi': pretasi,
        'nama': nama,
        'prodi': prodi,
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
    nama = request.GET.get('carinama')
    ordering = '-publikasi'
    form = FormPelanggaran()
    prodi = request.GET.get('cariprodi')
    
    pelanggaran = Pelanggaran.objects.all()

    if nama:
        pelanggaran = pelanggaran.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama)
        )

    if prodi:
        pelanggaran = pelanggaran.filter(prodi=prodi)

    pelanggaran = pelanggaran.order_by(ordering)

    paginator = Paginator(pelanggaran, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    pelanggaran = paginator.get_page(page_number)

    konteks = {
        'form': form,
        'pelanggaran': pelanggaran,
        'nama': nama,
        'prodi': prodi,
        'ordering': ordering,
    }

    return render(request, 'pelanggaran/tabel-pelanggaran.html', konteks)

def EditPelanggaranView(request, nim_Pelanggaran):
    pelanggaran = Pelanggaran.objects.get(nim=nim_Pelanggaran)
    template = 'pelanggaran/Edit-pelanggaran.html'
    if request.POST:
        form = FormPelanggaran(request.POST, request.FILES, instance=pelanggaran)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_pelanggaran', nim_Pelanggaran=nim_Pelanggaran)
    else:
        form = FormPelanggaran(instance=pelanggaran)
        konteks = {
            'form': form,
            'pelanggaran': pelanggaran,
        }
    return render(request, template, konteks)

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

    paginator = Paginator(data_beasiswa, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    data_beasiswa = paginator.get_page(page_number)

    konteks = {
        'data_beasiswa': data_beasiswa,
        'nama': nama,
        'ordering': ordering,
    }

    return render(request, 'Data_Beasiswa/data-beasiswa.html', konteks)

def Ubah_DataBeasiswa(request, id_Data_Beasiswa):
    data_beasiswa = Data_Beasiswa.objects.get(id=id_Data_Beasiswa)
    template = 'Data_Beasiswa/Ubah-DataBeasiwa.html'
    if request.POST:
        form = FormDataBeasiswa(request.POST, request.FILES, instance=data_beasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Ubah_DataBeasiswa', id_Data_Beasiswa=id_Data_Beasiswa)
    else:
        form = FormDataBeasiswa(instance=data_beasiswa)
        konteks = {
            'form': form,
            'data_beasiswa': data_beasiswa,
        }
    return render(request, template, konteks)

def Hapus_DataBeasiswa(request, id_Data_Beasiswa):
    data_beasiswa = Data_Beasiswa.objects.filter(id=id_Data_Beasiswa)
    data_beasiswa.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/Data-Beasiswa/')

# Start Penerima Beasiswa
def Tambah_Penerima(request):
    form = FormPenerima_Beasiswa()
    pesan = ""

    if request.POST:
        form = FormPenerima_Beasiswa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPenerima_Beasiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'Penerima_Beasiswa/tambah-penerima.html', konteks)
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
    
    return render(request, 'Penerima_Beasiswa/tambah-penerima.html', konteks)

def Penerima_BeasiswaView(request):
    nama = request.GET.get('cari')
    prodi = request.GET.get('cariprodi')
    ordering = '-publikasi'
    form = FormPenerima_Beasiswa()
    
    penerima = Penerima_Beasiswa.objects.all().order_by(ordering)

    if nama:
        penerima = penerima.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama) | Q(angkatan__icontains=nama)
        )

    if prodi:
        penerima = penerima.filter(prodi=prodi)

    paginator = Paginator(penerima, 2)  # Menampilkan 2 item per halaman
    page_number = request.GET.get('page')
    penerima = paginator.get_page(page_number)

    konteks = {
        'penerima': penerima,
        'prodi': prodi,
        'form': form,
        'nama': nama,
        'ordering': ordering,
    }
    return render(request, 'Penerima_Beasiswa/penerima-beasiswa.html', konteks)

def EditPenerima_Beasiswa(request, nim_Penerima_Beasiswa):
    penerima = Penerima_Beasiswa.objects.get(nim=nim_Penerima_Beasiswa)
    template = 'Penerima_Beasiswa/edit-penerima-beasiswa.html'
    if request.POST:
        form = FormPenerima_Beasiswa(request.POST, request.FILES, instance=penerima)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diperbaharui!')
            return redirect('Edit_Penerima', nim_Penerima_Beasiswa=nim_Penerima_Beasiswa)
    else:
        form = FormPenerima_Beasiswa(instance=penerima)
        konteks = {
            'form': form,
            'penerima': penerima,
        }
    return render(request, template, konteks)

def Hapus_Penerima_Beasiswa(request, nim_Penerima_Beasiswa):
    penerima = Penerima_Beasiswa.objects.filter(nim=nim_Penerima_Beasiswa)
    penerima.delete()

    messages.success(request, 'Data Berhasil Dihapus!')
    return redirect('/penerima-beasiswa/')

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

    paginator = Paginator(magang, 2) 
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

    paginator = Paginator(organisasi, 2) 
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
    nama = request.GET.get('cari')
    organisasi = request.GET.get('organisasi')
    ordering = '-publikasi'
    form = Form_Anggota_Organisasi()
    
    anggota = Anggota_Organisasi.objects.all().order_by(ordering)

    if nama:
        anggota = anggota.filter(
            Q(nama__icontains=nama) | Q(nim__icontains=nama) | Q(angkatan__icontains=nama)
        )

    if organisasi:
        anggota = anggota.filter(organisasi=organisasi)

    paginator = Paginator(anggota, 2) 
    page_number = request.GET.get('page')
    anggota = paginator.get_page(page_number)

    konteks = {
        'anggota': anggota,
        'organisasi': organisasi,
        'form': form,
        'nama': nama,
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