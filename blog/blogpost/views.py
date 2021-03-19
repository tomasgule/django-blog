from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Blogpost


class BlogpostListView(ListView):
    model = Blogpost
    template_name = "blogposts_list.html"


class BlogpostDetailView(DetailView):
    model = Blogpost
    template_name = "blogpost_detail.html"
    context_object_name = "blogpost"
