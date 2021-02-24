from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import Post
from theblog.form import CreateForm
from django.urls import reverse_lazy
from django.urls import reverse

class HomeView(ListView):
    model = Post
    template_name = 'post/home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post/article_details.html'

class AddPostView(CreateView):
    template_name = 'post/addpost.html'
    form_class = CreateForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post/updatepost.html'
    fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    template_name = 'post/deletepost.html'
    model = Post
    reverse_lazy = 'list'
