from django.urls import path
from. import views

urlpatterns = [
    #path("",views.base,name="apps"),
    #  path('site/', views.site, name='site'),
    
     path('index/', views.index, name='index'),
     path('caravan/', views.caravan, name='caravan'),
     path('login/', views.login, name='login'),
     path('treking/', views.treking, name='treking'),
     path('register/', views.register, name='register'),
     path('news/', views.news, name='news'),
         
     


    ]