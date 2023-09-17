from django.contrib import admin
from appkemahasiswaan.models import *

# MODEL UNTUK KEGIATAN.
class ArtikelAdmin(admin.ModelAdmin):
	list_display = ['judul', 'publikasi', 'Deskripsi', 'image']
	search_fields = ['judul', 'publikasi']
	list_per_page = 5
	readonly_fields=[
		'publikasi',
		'slug',
		'update',
		'status',
	]
admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Category)
admin.site.register(Prodi)

class PrestasiAdmin(admin.ModelAdmin):
    list_display = ['nim', 'nama', 'prodi', 'prestasi', 'tingkat', 'publikasi']
    search_fields = ['nim', 'nama']
    list_filter = ['prodi']

admin.site.register(Prestasi, PrestasiAdmin)

class PelanggaranAdmin(admin.ModelAdmin):
	list_display = ['nim', 'nama', 'prodi', 'angkatan', 'Jenis_pelanggaran', 'sanksi', 'publikasi']
	search_fields = ['nim', 'nama']
	list_filter = ['prodi']

admin.site.register(Pelanggaran, PelanggaranAdmin)

class DataBeasiswaAdmin(admin.ModelAdmin):
	readonly_fields=[
		'publikasi',
	]

admin.site.register(Data_Beasiswa, DataBeasiswaAdmin)

class BeasiswaInline(admin.TabularInline):
    model = Beasiswa
    extra = 1

class PenerimaBeasiswaAdmin(admin.ModelAdmin):
    inlines = [BeasiswaInline]
    list_display = ('nim', 'nama', 'angkatan', 'prodi', 'status', 'publikasi', 'gender')
    list_filter = ('angkatan', 'prodi', 'gender', 'status')
    search_fields = ('nim', 'nama')
    list_per_page = 20

admin.site.register(Penerima_Beasiswa, PenerimaBeasiswaAdmin)


class Mahasiswa_MagangAdmin(admin.ModelAdmin):
	readonly_fields=[
		'publikasi',
	]
admin.site.register(Mahasiswa_Magang, Mahasiswa_MagangAdmin)

class OrganisasiAdmin(admin.ModelAdmin):
	readonly_fields=[
		'publikasi',
	]
admin.site.register(Organisasi, OrganisasiAdmin)

class Anggota_OrganisasiAdmin(admin.ModelAdmin):
	readonly_fields=[
		'publikasi',
	]
admin.site.register(Anggota_Organisasi, Anggota_OrganisasiAdmin)