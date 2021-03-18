from django.contrib import admin
from django.urls import path

from blog.blogpost.views import BlogpostListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogposts/", BlogpostListView.as_view()),
]
