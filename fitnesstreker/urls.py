from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from fitnesstreker import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("users.urls", namespace="users")),
    path('', include("core.urls", namespace="core")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

