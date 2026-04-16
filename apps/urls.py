from django.urls import path
from . import views
from .views import (
    trekingList, trekingDetail,
    campingList, campingDetail,
    caravanList, caravanDetail,
    bookingCreate
)

urlpatterns = [
    # ---------- FRONTEND PAGES ----------
    path('index/', views.index, name='index'),
    path('news/', views.news, name='news'),

    path('treking_page/', views.treking_page, name='treking_page'),
    path('camping_page/', views.camping_page, name='camping_page'),
    path('caravan_page/', views.caravan_page, name='caravan_page'),

    path('detail/<str:type>/<int:pk>/', views.detail_page, name='detail-page'),

    # ---------- API ----------
    path('api/treking/', trekingList.as_view(), name='treking-list'),
    path('api/treking/<int:pk>/', trekingDetail.as_view(), name='treking-detail'),

    path('api/camping/', campingList.as_view(), name='camping-list'),
    path('api/camping/<int:pk>/', campingDetail.as_view(), name='camping-detail'),

    path('api/caravan/', caravanList.as_view(), name='caravan-list'),
    path('api/caravan/<int:pk>/', caravanDetail.as_view(), name='caravan-detail'),

    path('api/booking/', bookingCreate.as_view(), name='booking'),
]