from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admincamp/', admin.site.urls),

    # FRONTEND (HTML pages)
    path('', include('apps.urls')),  

    # API
    path('api/', include('apps.urls')),

    path('userregister/', include('userregister.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)