from django.urls import path
from webbuser.views import *
# from .view import *

urlpatterns = [
    path('artikel/', ArtikelList, name='artikel_list'),
    path('artikel-detail/<slug:slug_Artikel>/', ArtikelDetail, name='detail'),
    path('kategori/<slug:kategori_Artikel>/', ArtikelKategoriList, name='kategori'),
    path('ormawa/', OrganisasiList, name='orgawa_list'),
    path('personal-cv/', personal_cv, name='cv'),
    path('export-cv-to-pdf/', export_cv_to_pdf, name='export_cv_to_pdf'),
]
  