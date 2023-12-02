from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.forms import BaseInlineFormSet
from .models.files import File
from .models.folders import Folder


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'created_at', 'folder', ]
    list_display_links = ['id', 'created_at', ]
    list_filter = ['file', 'created_at', 'folder', ]
    search_fields = ['file', 'created_at', 'folder', ]
    ordering = ['folder', 'file']
    exclude = ('owner', )
    list_per_page = 10

    def get_form(self, request, obj=None, **kwargs):
        form = super(FileAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['folder'].queryset = Folder.objects.filter(owner=request.user)
        return form

    def get_queryset(self, request):
        qs = super(FileAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.creator = request.user
        obj.save()


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
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_id', 'name', ]
    list_display_links = ['id', ]
    list_editable = ['name']
    list_filter = ['name', ]
    search_fields = ['name', ]
    ordering = ['parent_id', 'name']
    # inlines = [FolderScopeInline]
    exclude = ('owner', )
    actions = ['set_parent_folder']
    list_per_page = 10

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(FolderAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['parent_id'].queryset = Folder.objects.filter(creator=request.user, parent_id__isnull=True)
    #     return form

    def get_queryset(self, request):
        qs = super(FolderAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()

    @admin.action(description='Сделать выбранные Папки - родителем')
    def set_parent_folder(self, request, qs: QuerySet):
        count_updated = qs.update(parent_id=None)
        self.message_user(
            request,
            f'Родительская папка назначена для {count_updated} записи(ей)'
        )
