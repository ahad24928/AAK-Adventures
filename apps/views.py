import requests
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Treking, Camping, Caravan
from .serializers import TrekingSerializer, CampingSerializer, CaravanSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser

# -------- NORMAL VIEWS --------

def index(request):
    return render(request, "apps/index.html", )

def caravan(request):
    return render(request, "apps/caravan.html")

def login(request):   
    return render(request, "apps/login.html")

def register(request):
    return render(request, "apps/register.html")

def news(request):
    return render(request, "apps/news.html")


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
    if type == "trek":
        obj = get_object_or_404(Treking, id=pk)

    elif type == "camp":
        obj = get_object_or_404(Camping, id=pk)

    else:  
        obj = get_object_or_404(Caravan, id=pk)

    return render(request, "apps/detail.html", {"obj": obj})


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
