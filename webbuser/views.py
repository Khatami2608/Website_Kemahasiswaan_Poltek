from django.shortcuts import render
from django.views.generic import *
from appkemahasiswaan.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from urllib.parse import urlencode
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import FileResponse
from xhtml2pdf import pisa
from io import BytesIO

def ArtikelList(request):
    ordering = '-publikasi'
    tb_artikel = Artikel.objects.all().order_by(ordering)
    kategori = Artikel.objects.all()
    search = request.GET.get('cari')
    cari_tgl = request.GET.get('tanggal')

    if search:
        tb_artikel = tb_artikel.filter(
            Q(judul__icontains=search) | Q(kategori__icontains=search)
        )
    if cari_tgl:
        tb_artikel = tb_artikel.filter(publikasi__date=cari_tgl)

    paginator = Paginator(tb_artikel, 2)
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

def OrganisasiList(request):
    organisasi = Organisasi.objects.all()

    konteks = {
        'organisasi': organisasi,
    }
    return render(request, 'organisasi_user/organisasi_list.html', konteks)

def personal_cv(request):
    personal_info = PersonalInfo.objects.first()  # Mengambil data personal info (Anda bisa sesuaikan dengan kebutuhan)
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
