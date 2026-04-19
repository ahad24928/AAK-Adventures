from django.urls import path
from .views import ( trekingList, trekingDetail,  campingList, campingDetail,caravanList, caravanDetail,
                     NewsListCreateAPIView, NewsDetailAPIView, bookingCreate)

urlpatterns = [
    path('treking/', trekingList.as_view()),
    path('treking/<int:pk>/', trekingDetail.as_view()),

    path('camping/', campingList.as_view()),
    path('camping/<int:pk>/', campingDetail.as_view()),

    path('caravan/', caravanList.as_view()),
    path('caravan/<int:pk>/', caravanDetail.as_view()),

    path('news/', NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailAPIView.as_view()),

    path('booking/', bookingCreate.as_view()),
]