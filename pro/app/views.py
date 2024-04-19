from django.shortcuts import render
from .models import TODO ,CustomUser
from .forms import TODOForm ,TODOFormCaptcha
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import CustomUserCreateForm

class CreateUser(CreateView):
    model = CustomUser
    template_name = 'createuser.html'
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('index')


class TODOListView(ListView):
    model = TODO
    template_name = 'index.html'
    context_object_name = 'todos'
    paginate_by=2

class TODODetail(DetailView):
    model = TODO
    template_name = 'detail.html'
    context_object_name = 'todo'


class TODODelete(DeleteView):
    model = TODO
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

class TODOUpdate(UpdateView):
    model = TODO
    template_name = 'update.html'
    form_class = TODOForm
    success_url = reverse_lazy('index')


class TODOCreate(CreateView):
    model = TODO
    template_name = 'create.html'
    form_class = TODOFormCaptcha
    success_url = reverse_lazy('index')
    
    

