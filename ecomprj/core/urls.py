from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_roots=settings.STATIC_ROOTS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOTS)