from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('treking_page/', views.treking_page, name='treking_page'),
    path('camping_page/', views.camping_page, name='camping_page'),
    path('caravan_page/', views.caravan_page, name='caravan_page'),
    path('news/', views.news_page, name='news_page'),

    path('detail/<str:type>/<int:pk>/', views.detail_page, name='detail-page'),
    path('detail/<str:type>/<int:pk>/comment/', views.add_comment, name='add_comment'), 

    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    
    path('contact/', views.contact, name='contact'),
]