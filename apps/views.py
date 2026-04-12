from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# def site(request):
# 	return render(request, "apps/site.html")


def index(request):
	return render(request, "apps/index.html")

def caravan(request):
	return render(request, "apps/caravan.html")

def login(request):
	return render(request, "apps/login.html")

# @login_required(login_url='login')     
def treking(request):
	 return render(request, "apps/treking.html")
    # return HttpResponse("This page is restricted.")

def register(request):
	return render(request, "apps/register.html")

def news(request):
	return render(request, "apps/news.html")


























