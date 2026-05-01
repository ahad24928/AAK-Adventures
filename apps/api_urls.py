from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( trekingList, trekingDetail,  campingList, campingDetail,caravanList, caravanDetail,
                     NewsListCreateAPIView, NewsDetailAPIView, BookingViewSet)

router = DefaultRouter()
router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('treking/', trekingList.as_view()),
    path('treking/<int:pk>/', trekingDetail.as_view()),

    path('camping/', campingList.as_view()),
    path('camping/<int:pk>/', campingDetail.as_view()),

    path('caravan/', caravanList.as_view()),
    path('caravan/<int:pk>/', caravanDetail.as_view()),

    path('news/', NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailAPIView.as_view()),

    path('', include(router.urls)),
]