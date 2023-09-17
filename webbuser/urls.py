from django.urls import path
from webbuser.views import *
# from .view import *

urlpatterns = [
    path('artikel/', ArtikelList, name='artikel_list'),
    path('artikel-detail/<slug:slug_Artikel>/', ArtikelDetail, name='detail'),
    path('kategori/<slug:kategori_Artikel>/', ArtikelKategoriList, name='kategori'),
    path('ormawa/', OrganisasiList, name='orgawa_list'),
    path('list-beasiswa/', ListBeasiswa, name='beasiswa_list'),
    path('export-cv-to-pdf/', export_cv_to_pdf, name='export_cv_to_pdf'),
    # path('tambah_data/', tambah_data, name='tambah_data'),
    path('home/', home, name='home'),
    path('profil/', profile, name='profil'),
    # path('create_profile/', create_profile, name='create_profile')
    # cv
    path('personal-cv/<int:personal_info_id>/', personal_cv, name='personal_cv'),
    path('input_personal_info/', input_personal_info, name='input_personal_info'),
    path('input_pendidikan/<int:personal_info_id>/', input_pendidikan, name='input_pendidikan'),
    path('input_skill/<int:personal_info_id>/', input_skill, name='input_skill'),
    path('input_training/<int:personal_info_id>/', input_training, name='input_training'),
    # data SKPI
    path('tambah-info-mahasiswa/', Addskpi_Personal, name='skpi_personal'),
    path('data-skpi/<int:data_skpi_nim>/', ViewSKPI, name='data_skpi'),
    path('Edit-info-mahasiswa/<int:data_skpi_nim>/', Edit_skpi, name='Edit_data_skpi'),
    path('tambah-organisasi/<int:data_skpi_nim>/', tambah_organisasi, name='tambah_organisasi'),
    path('tambah-pelatihan/<int:data_skpi_nim>/', tambah_pelatihan, name='pelatihan'),
    path('tambah-penghargaan/<int:data_skpi_nim>/', tambah_penghargaan, name='penghargaan'),
    path('tambah-sertifikasi/<int:data_skpi_nim>/', tambah_sertifikasi, name='sertifikasi'),
    path('tambah-data-beasiswa/<int:data_skpi_nim>/', tambah_beasiswa, name='tb_beasiswa'),
    path('templates/', tes_template),
]
  