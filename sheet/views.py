from django.shortcuts import render
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import *
# from .importer import ad_read, ip_read, xml_to_dict
# from .filters import ADFilter, ReportFilter, FormFilter
import xml.etree.ElementTree as ET
# from django.core.paginator import Paginator
# from .forms import CNForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
# from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.core.cache import cache  # импортируем наш кэш
from datetime import datetime, timezone, timedelta
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.shortcuts import render
from django.db.models import Q


# logger = logging.getLogger(__name__)


class Tips(ListView):
	model = TipsText
	template_name = 'tips.html'
	context_object_name = 'tips'
	ordering = ['-priority']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = self.kwargs.get('slug', '')
		context["tips_list"] = TipsText.objects.select_related('category').filter(category__slug=category).\
			filter(tip_visible=True).order_by('-priority')
		return context


class Category(ListView):
	model = TipsCategory
	template_name = 'category.html'
	context_object_name = 'categories'
	ordering = ['-category_priority']

	def get_queryset(self):
		queryset = TipsCategory.objects.filter(category_visible=True)
		return queryset


def about(request):
	return render(request, "about.html")

