from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('khan_admin/', admin.site.urls),

    # FRONTEND (HTML pages)
    path('', include('apps.urls')),  

    # API
    path('api/', include('apps.api_urls')),

     # Auth system (login/register)
    path('auth/', include('userregister.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)