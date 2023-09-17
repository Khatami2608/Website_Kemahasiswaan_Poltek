from django.contrib import admin
from .models import *

class PendidikanInline(admin.TabularInline):
    model = Pendidikan
    extra = 1

class TrainingInline(admin.TabularInline):
    model = Training
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class PersonalInfoAdmin(admin.ModelAdmin):
    inlines = [PendidikanInline, TrainingInline, SkillInline]
    list_display = ('first_name', 'last_name', 'email', 'nomer_hp')

admin.site.register(PersonalInfo, PersonalInfoAdmin)

admin.site.register(data_skpi)
admin.site.register(organisasi)