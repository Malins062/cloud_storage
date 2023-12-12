from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.forms import BaseInlineFormSet
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models.files import File
from .models.folders import Folder


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', ]
    list_display_links = ['id', 'created_at', ]
    list_filter = ['content', 'created_at', ]
    search_fields = ['content', 'created_at', ]
    ordering = ['content']
    # exclude = ('owner', )
    readonly_fields = ['owner', 'created_at', 'updated_at', ]
    list_per_page = 20

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(FileAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['folder'].queryset = Folder.objects.filter(owner=request.user)
    #     return form

    # def get_queryset(self, request):
    #     qs = super(FileAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)
    #
    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'owner', None) is None:
    #         obj.creator = request.user
    #     obj.save()


class FolderScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        folders = [f.cleaned_data.get('folder') for f in self.forms
                   if f.cleaned_data.get('folder') and f.cleaned_data.get('DELETE') is False]

        if len(folders) != len(set(folders)):
            raise ValidationError(f'Ошибка: папки не должны повторяться!')
        return super().clean()


class FolderScopeInline(admin.TabularInline):
    model = Folder
    extra = 0
    min_num = 1
    formset = FolderScopeInlineFormset


@admin.register(Folder)
class FolderAdmin(DjangoMpttAdmin):
    list_display = [
        # 'id', 'parent_id', 'tree_id', 'level',
        'name',
        'owner',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'name',
    ]
    # list_editable = ['name']
    list_filter = ['name', ]
    search_fields = ['name', ]
    # ordering = ['tree_id', 'level', 'parent_id', 'name']
    # ordering = ['name']
    # inlines = [FolderScopeInline]
    # exclude = ('owner', )
    readonly_fields = ['owner', 'created_at', 'updated_at', ]
    # actions = ['set_parent_folder']
    list_per_page = 20

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(FolderAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['parent_id'].queryset = Folder.objects.filter(creator=request.user, parent_id__isnull=True)
    #     return form

    # def get_queryset(self, request):
    #     qs = super(FolderAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)
    #
    # def save_model(self, request, obj, form, change):
    #     if getattr(obj, 'owner', None) is None:
    #         obj.owner = request.user
    #     obj.save()
    #
    # @admin.action(description='Сделать выбранные Папки - родителем')
    # def set_parent_folder(self, request, qs: QuerySet):
    #     count_updated = qs.update(parent_id=None)
    #     self.message_user(
    #         request,
    #         f'Родительская папка назначена для {count_updated} записи(ей)'
    #     )
