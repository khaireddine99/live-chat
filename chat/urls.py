# chat/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.customLogin, name='custom_login'),
    path('new_post', views.create_post, name='new_post'),
    path('posts', views.post_list, name='posts'),
    path('posts/<int:post_id>', views.post, name='post')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)