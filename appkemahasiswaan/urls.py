from django.urls import path
from appkemahasiswaan.views import *
# from .view import *

urlpatterns = [
    path('tambah-artikel/', tambah_artikel, name='tambah_artikel'),
    path('tabel-artikel/', Tabel_ArtikelView, name='tabel_artikel'),
    path('edit-artikel/<int:id_Artikel>/', Edit_Artikel, name='edit_artikel'),
    path('hapus-artikel/<int:id_Artikel>/', Hapus_Artikel, name='hapus_artikel'),
    path('prestasi/', PrestasiView, name='prestasi'),
    path('tambah-prestasi/', AddPrestasiView, name='Addprestasi'),
    path('Edit-prestasi/<int:nim_Prestasi>/', EditPrestasiView, name='Edit_prestasi'),
    path('Hapus-prestasi/<int:nim_Prestasi>/', HapusPrstasiView, name='hapus_prestasi'),
    path('tambah-pelanggaran/', AddPelanggaranView, name='tambah_pelanggaran'),
    path('pelanggaran/', PelanggaranView, name='pelanggaran'),
    path('Edit-pelanggaran/<int:nim_Pelanggaran>/', EditPelanggaranView, name='Edit_pelanggaran'),
    path('Hapus-pelanggaran/<int:nim_pelanggaran>/', HapusPelanggaranView, name='hapus_pelanggaran'),
    path('Tambah-Data-Beasiswa/', AddDataBeasiswa, name='AddData_Beasiswa'),
    path('Data-Beasiswa/', DataBeasiswa, name='Data_Beasiswa'),
    path('Edit-Data-Beasiswa/<int:id_Data_Beasiswa>/', Ubah_DataBeasiswa, name='Ubah_DataBeasiswa'),
    path('hapus-DataBeasiswa/<int:id_Data_Beasiswa>/', Hapus_DataBeasiswa, name='Hapus_DataBeasiswa'),
    path('tambah-penerima-beasiswa/', Tambah_Penerima, name='Tambah_Penerima'),
    path('penerima-beasiswa/', Penerima_BeasiswaView, name='Penerima_Beasiswa'),
    path('edit-penerima-beasiswa/<int:nim_Penerima_Beasiswa>/', EditPenerima_Beasiswa, name='Edit_Penerima'),
    path('hapus-penerima-beasiswa/<int:nim_Penerima_Beasiswa>/', Hapus_Penerima_Beasiswa, name='Hapus_Penerima'),
    path('tambah-mahasiswa-magang/', Tambah_Mhs_Magang, name='Tambah_Magang'),
    path('mahasiswa-ppi/', Mahasiswa_MagangView, name='mahasiswa_ppi'),
    path('edit-mahasiswa-ppi/<int:nim_Mahasiswa_Magang>/', Edit_MagangView, name='Edit_Mahasiswa_PPI'),
    path('hapus-mahasiswa-ppi/<int:nim_Mahasiswa_Magang>/', Hapus_Magang, name='Hapus_Magang'),
    path('organisasi/', OrganisasiView, name='organisasi'),
    path('tambah-organisasi/', Tambah_Organisasi, name='Tambah_Organisasi'),
    path('edit-organisasi/<uuid:id_organisasi_Organisasi>/', Edit_Organisasi, name='Edit_Organisasi'),
    path('hapus-organisasi/<uuid:id_organisasi_Organisasi>/', Hapus_Organisasi, name='Hapus_Organisasi'),
    path('tambah-anggota/', Tambah_Anggota, name='tambah_anggota'),
    path('anggota-organisasi/', AnggotaView, name='anggota_organisasi'),
    path('edit-anggota/<uuid:id_anggota_Anggota_Organisasi>/', Edit_AnggotaView, name='Edit_Anggota'),
    path('hapus-anggota/<uuid:id_anggota_Anggota_Organisasi>/', Hapus_AnggotaView, name='Hapus_Anggota'),
]
  