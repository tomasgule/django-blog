from django.shortcuts import render
from django.views.generic import ListView

from .models import Blogpost


class BlogpostListView(ListView):
    model = Blogpost
    template_name = "blogposts_list.html"