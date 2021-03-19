from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from blog.blogpost.views import BlogpostListView
from blog.blogpost.views import BlogpostDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BlogpostListView.as_view(), name="blogpost-list"),
    path(
        "blogpost/<int:pk>/",
        BlogpostDetailView.as_view(),
        name="blogpost-detail",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
