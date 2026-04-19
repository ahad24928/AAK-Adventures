import requests
#  DJANGO  IMPORTS
from datetime import datetime
from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#  DJANGO REST FRAMEWORK IMPORTS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import (SessionAuthentication, BasicAuthentication)
from rest_framework.permissions import (AllowAny, IsAuthenticated)
#  LOCAL APP IMPORTS
from .models import ( Treking, Camping, Caravan, Booking, Country, HotelComment, News)
from .serializers import (TrekingSerializer, CampingSerializer, CaravanSerializer, BookingSerializer, NewsSerializer)



# -------- NORMAL VIEWS --------
def index(request):
    cities = Country.objects.all()
    rent = Caravan.objects.all()

    return render(request, "apps/index.html", {"cities": cities, "rent":rent})

def caravan(request):
    return render(request, "apps/caravan.html")

def news_page(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, "apps/news.html", {"news": news})

# ================= TREKKING =================

def treking_page(request):
    data = Treking.objects.all()
    return render(request, "apps/treking.html", {"data": data})

# ================= CAMPING =================
def camping_page(request):
    data_camp = Camping.objects.all()  
    return render(request, "apps/camping.html", {"data_camp": data_camp})

# ================= CARAVAN =================
def caravan_page(request):
    data_caravan = Caravan.objects.all()  
    return render(request, "apps/caravan.html", {"data_caravan": data_caravan})


def detail_page(request, type, pk):
    if type == "camping":
        obj = Camping.objects.get(id=pk)
    elif type == "treking":
        obj = Treking.objects.get(id=pk)
    else:
        obj = Caravan.objects.get(id=pk)

    comments = HotelComment.objects.filter(
        item_type=type,
        item_id=pk,
        parent__isnull=True
    ).order_by('-created_at')

    return render(request, "apps/detail.html", {
        "obj": obj,
        "type": type,
        "comments": comments
    })

@login_required(login_url='login')
def add_comment(request, type, pk):
    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")

        parent = None
        if parent_id:
            parent = get_object_or_404(HotelComment, id=parent_id)

        HotelComment.objects.create(
            user=request.user,
            item_type=type,
            item_id=pk,
            content=content,
            parent=parent
        )

        messages.success(request, "Comment added successfully")

    return redirect('detail-page', type=type, pk=pk)


@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "apps/my_bookings.html", {
        "bookings": bookings
    })

# -------- API VIEWS --------

class trekingList(ListCreateAPIView):
    queryset = Treking.objects.all()
    serializer_class = TrekingSerializer


class trekingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Treking.objects.all()
    serializer_class = TrekingSerializer

   
# camping api

class campingList(ListCreateAPIView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer


class campingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

# caravan api

class caravanList(ListCreateAPIView):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer

class caravanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer

# LIST + CREATE
class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

# RETRIEVE + UPDATE + DELETE
class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class bookingCreate(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




