import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Treking, Camping, Caravan
from .serializers import TrekingSerializer, CampingSerializer, CaravanSerializer

# -------- NORMAL VIEWS --------

def index(request):
    return render(request, "apps/index.html")

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
    

# -------- API VIEWS --------

@api_view(['GET', 'POST'])
def treking_list(request):

    if request.method == 'GET':
        data = Treking.objects.all()
        serializer = TrekingSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrekingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)  


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def treking_detail(request, id):
    treking = get_object_or_404(Treking, id=id)

    if request.method == 'GET':
        serializer = TrekingSerializer(treking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrekingSerializer(treking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        serializer = TrekingSerializer(treking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        treking.delete()
        return Response({"message": "Deleted successfully"})

# camping api

@api_view(['GET', 'POST'])
def camping_list(request):

    if request.method == 'GET':
        data = Camping.objects.all()
        serializer = CampingSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CampingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors) 


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def camping_detail(request, id):
    camping = get_object_or_404(Camping, id=id)

    if request.method == 'GET':
        serializer = CampingSerializer(camping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampingSerializer(camping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        serializer = CampingSerializer(camping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        camping.delete()
        return Response({"message": "Deleted successfully"})

@api_view(['GET', 'POST'])
def caravan_list(request):
    
    if request.method == 'GET':
        data = Caravan.objects.all()
        serializer = CaravanSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CaravanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def caravan_detail(request, id):
    caravan = get_object_or_404(Caravan, id=id)

    if request.method == 'GET':
        serializer = CaravanSerializer(caravan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CaravanSerializer(caravan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        serializer = CaravanSerializer(caravan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        caravan.delete()
        return Response({"message": "Deleted successfully"})