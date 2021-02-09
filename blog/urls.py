#blog/urls.py
from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ...
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
    path('upload/', views.image_upload_view),
]