from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blat
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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
	template_name  = 'blat/my_post.html'

class NewBlatView(CreateView):
	model = Blat 
	fields = ['title', 'text']
	template_name = 'blat/create_blat.html'
	success_url = "/my/"
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(NewBlatView, self).form_valid(form)
class EditBlatView(UpdateView):
	model = Blat 
	fields = ['title', 'text']
	success_url = "/my/"
	template_name = 'blat/edit.html'
class TemplateViews(TemplateView):
	template_name = 'blat/user_info.html'
class BlogDeleteView(DeleteView):
    model = Blat
    template_name = 'blat/delete.html'
    success_url = reverse_lazy('home')