from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class TipsCategory(models.Model):
	category = models.CharField(max_length=32, unique=True)
	slug = models.SlugField(max_length=32, unique=True, db_index=True, verbose_name="URL")
	category_priority = models.PositiveSmallIntegerField()
	category_author = models.ForeignKey(User, on_delete=models.PROTECT)
	category_whenCreated = models.DateTimeField(auto_now_add=True)
	category_visible = models.BooleanField(default=True)


	# Печатаем красиво
	def __str__(self):
		return f'{self.slug}'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.category)
		super(TipsCategory, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("tips", kwargs={"slug": self.slug})


class TipsText(models.Model):
	category = models.ForeignKey(TipsCategory, on_delete=models.PROTECT)
	section_tag = models.CharField(max_length=64)
	section = models.PositiveSmallIntegerField()
	priority = models.PositiveSmallIntegerField()
	# text = RichTextField(config_name='awesome_ckeditor')
	text = CKEditor5Field('Text', config_name='extends')
	author = models.ForeignKey(User, on_delete=models.PROTECT)
	whenCreated = models.DateTimeField(auto_now_add=True)
	tip_visible = models.BooleanField(default=True)
	dimension = models.PositiveSmallIntegerField(default=1)

	# Печатаем красиво
	def __str__(self):
		return f'{self.category}-{self.section_tag}: {self.section}-{self.priority} ({self.dimension})'
