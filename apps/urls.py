from django.urls import path
from. import views

urlpatterns = [
    # path("",views.base,name="apps"),
    # path('site/', views.site, name='site'),
    
     path('index/', views.index, name='index'),
     path('login/', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('news/', views.news, name='news'),
     path('treking-page/', views.treking_page, name='treking_page'),
     path('camping-page/', views.camping_page, name='camping_page'),
     path('caravan-page/', views.caravan_page, name='caravan_page'),


     path('treking/', views.treking_list),
     path('treking/<int:id>/', views.treking_detail),
     path('camping/', views.camping_list),
     path('camping/<int:id>/', views.camping_detail),
     path('caravan/', views.caravan_list),
     path('caravan/<int:id>/', views.caravan_detail),

    ]