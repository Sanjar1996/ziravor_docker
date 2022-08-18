from django.contrib import admin
from .models import XodimModels, YangiliklarModel, FloraTypeModel, FloraModel, DockModel, ElektronTypeModels, \
    ElektronModels


@admin.register(XodimModels)
class XodimAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(YangiliklarModel)
class YangiliklarAdmin(admin.ModelAdmin):
    field = ('sub_title', 'title', 'data', 'image', 'text')


@admin.register(FloraTypeModel)
class FloraTypeAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(FloraModel)
class FloraAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(DockModel)
class DockAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(ElektronTypeModels)
class ElektronTypeAdmin(admin.ModelAdmin):
    field = ('__all__')


@admin.register(ElektronModels)
class ElektronAdmin(admin.ModelAdmin):
    field = ('__all__')
