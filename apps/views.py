import requests
from datetime import datetime
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Treking, Camping, Caravan, Booking, Country
from .serializers import TrekingSerializer, CampingSerializer, CaravanSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# -------- NORMAL VIEWS --------

def index(request):
    cities = Country.objects.all()
    return render(request, "apps/index.html", {"cities": cities})

def caravan(request):
    return render(request, "apps/caravan.html")

def news(request):
    return render(request, "apps/news.html")

def adventure_page(request):
    return render(request, "apps/adventure.html")


def treking_page(request):
    api_url = "http://127.0.0.1:8000/api/treking/"
    
    response = requests.get(api_url)
    data = response.json()

    return render(request, "apps/treking.html", {"data": data})

def camping_page(request):
    api_url = "http://127.0.0.1:8000/api/camping/"
    
    response = requests.get(api_url)
    data_camp = response.json()

    return render(request, "apps/camping.html", {"data_camp": data_camp})

def caravan_page(request):
    api_url = "http://127.0.0.1:8000/api/caravan/"
    
    response = requests.get(api_url)
    data_caravan = response.json()

    return render(request, "apps/caravan.html", {"data_caravan": data_caravan})


def detail_page(request, type, pk):
    if type == "camping":
        obj = Camping.objects.get(id=pk)
    elif type == "treking":
        obj = Treking.objects.get(id=pk)
    else:
        obj = Caravan.objects.get(id=pk)

    return render(request, "apps/detail.html", {
        "obj": obj,
        "type": type
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

class bookingCreate(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    authentication_classes = []
    permission_classes = [AllowAny]




