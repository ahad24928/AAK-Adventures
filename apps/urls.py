from django.urls import path
from. import views
from .views import (
    trekingList, trekingDetail, 
    campingList, campingDetail,
    caravanList, caravanDetail
) 


urlpatterns = [
    # path("",views.base,name="apps"),
    # path('site/', views.site, name='site'),
    
     path('index/', views.index, name='index'),
     path('login/', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('news/', views.news, name='news'),
     path('treking_page/', views.treking_page, name='treking_page'),
     path('camping_page/', views.camping_page, name='camping_page'),
     path('caravan_page/', views.caravan_page, name='caravan_page'),
     path('detail/<str:type>/<int:pk>/', views.detail_page, name='detail-page'),


     path('treking/', trekingList.as_view(), name='treking-list'),
     path('treking/<int:pk>/', trekingDetail.as_view(), name='treking-detail'),

     path('camping/', views.campingList.as_view(), name='camping-list'),
     path('camping/<int:pk>/', views.campingDetail.as_view(), name='camping-detail'),

     path('caravan/', views.caravanList.as_view(), name='caravan-list'),
     path('caravan/<int:pk>/', views.caravanDetail.as_view(), name='caravan-detail'),

    ]