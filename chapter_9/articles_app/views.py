from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "author", "body"]
    template_name = "article_create.html"
    success_url = reverse_lazy("article_list_view") # I assume this goes to the homepage of this app, which would be the ArticleListView.

class ArticleUpdateView(UpdateView):
    model = Article
    fields = [
        "title",
        "body",
    ]
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list_view") # I assume this goes to the homepage of this app, which would be the ArticleListView.