from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Treking
from .serializers import TrekingSerializer

# def site(request):
# 	return render(request, "apps/site.html")


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


@api_view(['GET', 'PUT', 'DELETE'])
# @login_required(login_url='login')     
def treking_detail(request, id):
    try:
        trek = Treking.objects.get(id=id)
    except Treking.DoesNotExist:
        return Response({'error': 'Not found'})

    if request.method == 'GET':
        serializer = TrekingSerializer(trek)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrekingSerializer(trek, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        trek.delete()
        return Response({'message': 'Deleted successfully'})
    # return HttpResponse("This page is restricted.")



























