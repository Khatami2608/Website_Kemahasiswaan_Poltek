from django.urls import path
from appkemahasiswaan.views import *
# from .view import *

urlpatterns = [
    # Artikel
    path('tambah-kategori/', tambah_kategori, name='tambah_kategori'),
    path('hapus-kategori/', kategori, name='kategori'),
    path('hapus-kategori/<int:id_kategori>/', hapus_kategori, name='hapus_kategori'),
    path('tambah-artikel/', tambah_artikel, name='tambah_artikel'),
    path('tabel-artikel/', Tabel_ArtikelView, name='tabel_artikel'),
    path('edit-artikel/<int:id_Artikel>/', Edit_Artikel, name='edit_artikel'),
    path('hapus-artikel/<int:id_Artikel>/', Hapus_Artikel, name='hapus_artikel'),
    # path('tambah-artikel/', tambah_kategori, name='tambah_kategori'),
    path('/publish/<int:artikel_id>/', publish_artikel, name='publish_artikel'),
    path('/draft/<int:artikel_id>/', draft_artikel, name='draft_artikel'),
    # Prestasi
    path('prestasi/', PrestasiView, name='prestasi'),
    path('tambah-prestasi/', AddPrestasiView, name='Addprestasi'),
    path('Edit-prestasi/<int:nim_Prestasi>/', EditPrestasiView, name='Edit_prestasi'),
    path('Hapus-prestasi/<int:nim_Prestasi>/', HapusPrstasiView, name='hapus_prestasi'),
    # Pelanggaran
    path('tambah-pelanggaran/', AddPelanggaranView, name='tambah_pelanggaran'),
    path('pelanggaran/', PelanggaranView, name='pelanggaran'),
    path('Edit-Pelanggaran/<int:nim_pelanggaran>/', EditPelanggaranView, name='edit_pelanggaran'),
    path('Hapus-pelanggaran/<int:nim_pelanggaran>/', HapusPelanggaranView, name='hapus_pelanggaran'),
    # Beasiswa
    path('Tambah-Data-Beasiswa/', AddDataBeasiswa, name='AddData_Beasiswa'),
    path('Data-Beasiswa/', DataBeasiswa, name='Data_Beasiswa'),
    path('Edit-Data-Beasiswa/<str:Data_Beasiswa_nama>/', Ubah_DataBeasiswa, name='Ubah_Data_Beasiswa'),
    path('hapus-Data-Beasiswa/<str:Data_Beasiswa_nama>/', Hapus_DataBeasiswa, name='Hapus_DataBeasiswa'),
    # Penerima Beasiswa
    path('tambah-penerima-beasiswa/', Tambah_Penerima, name='tambah_penerima'),
    path('tambah-beasiswa/<int:nim_penerima>/', Tambah_Beasiswa, name='tambah_beasiswa'),
    path('penerima-beasiswa/', Penerima_BeasiswaView, name='Penerima_Beasiswa'),
    path('edit-penerima/<int:nim_penerima>/', edit_penerima, name='edit_penerima'),
    path('edit-beasiswa/<int:id_beasiswa>/', edit_beasiswa, name='edit_beasiswa'),
    path('hapus-penerima-beasiswa/<int:nim_Penerima_Beasiswa>/', Hapus_Penerima_Beasiswa, name='Hapus_Penerima'),
    path('detail-penerima-beasiswa/<int:nim_Penerima_Beasiswa>/', DetailPenerima, name='detail_penerima'),
    # PPI
    path('tambah-mahasiswa-magang/', Tambah_Mhs_Magang, name='Tambah_Magang'),
    path('mahasiswa-ppi/', Mahasiswa_MagangView, name='mahasiswa_ppi'),
    path('edit-mahasiswa-ppi/<int:nim_Mahasiswa_Magang>/', Edit_MagangView, name='Edit_Mahasiswa_PPI'),
    path('hapus-mahasiswa-ppi/<int:nim_Mahasiswa_Magang>/', Hapus_Magang, name='Hapus_Magang'),
    # Organisasi
    path('organisasi/', OrganisasiView, name='organisasi'),
    path('tambah-organisasi/', Tambah_Organisasi, name='Tambah_Organisasi'),
    path('edit-organisasi/<uuid:id_organisasi_Organisasi>/', Edit_Organisasi, name='Edit_Organisasi'),
    path('hapus-organisasi/<uuid:id_organisasi_Organisasi>/', Hapus_Organisasi, name='Hapus_Organisasi'),
    # Anggota
    path('tambah-anggota/', Tambah_Anggota, name='tambah_anggota'),
    path('anggota-organisasi/', AnggotaView, name='anggota_organisasi'),
    path('edit-anggota/<uuid:id_anggota_Anggota_Organisasi>/', Edit_AnggotaView, name='Edit_Anggota'),
    path('hapus-anggota/<uuid:id_anggota_Anggota_Organisasi>/', Hapus_AnggotaView, name='Hapus_Anggota'),
    # User 
    path('tambah-user/', tambah_user, name='tambah_user'),
    path('tabel-user/', UserView, name='tabel_user'),
]
  