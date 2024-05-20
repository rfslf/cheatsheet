from django.contrib import admin
from .models import TipsText, TipsCategory
from django import forms
# from ckeditor.widgets import CKEditorWidget


class TipsCategoryAdmin(admin.ModelAdmin):
	list_display = ('category', 'category_priority', 'category_author', 'category_whenCreated',)
	search_fields = ('category', 'category_author',)


class TextAdminForm(forms.ModelForm):
	# content = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = TipsText
		fields = '__all__'


class TextAdmin(admin.ModelAdmin):
	form = TextAdminForm
	list_display = ('category','section_tag','section','priority','dimension')
	search_fields = ('section_tag',)


admin.site.register(TipsText, TextAdmin)
admin.site.register(TipsCategory, TipsCategoryAdmin)
