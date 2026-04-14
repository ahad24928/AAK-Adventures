import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Treking
from .serializers import TrekingSerializer

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