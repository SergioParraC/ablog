from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Post
from theblog.form import CreateForm
from django.urls import reverse_lazy
from django.urls import reverse

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    template_name = 'addpost.html'
    form_class = CreateForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'updatepost.html'
    fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    template_name = 'deletepost.html'
    model = Post
    reverse_lazy = 'list'