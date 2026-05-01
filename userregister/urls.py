from django.urls import path
from . import views
from . views import logout_view


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # API
    path('api/register/', views.register_api, name='register_api'),
]


