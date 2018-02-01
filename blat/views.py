from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Blat
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
	model = Blat 
	template_name = 'blat/blat.html'
	context_object_name = 'blat_list'
	def get_queryset(self):
		return Blat.objects.order_by('-created_on')[:20]
class DetailView(DetailView):
	model = Blat
	template_name = 'blat/detail.html'
	context_object_name = 'blat'
class MyView(IndexView):
	def get_queryset(self):
		return Blat.objects.filter(created_by=self.request.user.id).order_by('-created_on')[:20]
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(MyView, self).dispatch(*args, **kwargs)
class NewBlatView(CreateView):
	model = Blat 
	fields = ['text', 'via']
	success_url = "/my/"
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(NewBlatView, self).form_valid(form)
class EditBlatView(UpdateView):
	model = Blat 
	fields = ['text', 'via']
	success_url = "/my/"