from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import TipsText


class TipsForm(forms.ModelForm):
	"""Form for tips into cheatsheet"""

	class Meta:
		model = TipsText
		# fields = '__all__'
		fields = ['section_tag', 'section', 'priority', 'text', 'dimension']
		widgets = {
			"text": CKEditor5Widget(
				attrs={"class": "django_ckeditor_5"}, config_name="tip"
			)
		}
