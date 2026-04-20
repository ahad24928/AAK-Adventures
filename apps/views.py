import requests
#  DJANGO  IMPORTS
from datetime import datetime
from django.db.models import Q
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
from .models import ( Treking, Camping, Caravan, Booking, Country, HotelComment, Contact, News)
from .serializers import (TrekingSerializer, CampingSerializer, CaravanSerializer, BookingSerializer, NewsSerializer)

# -------- NORMAL VIEWS --------
def index(request):
    cities = Treking.objects.all()
    rent = Caravan.objects.all()

    return render(request, "apps/index.html", {"cities": cities, "rent":rent})

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

# ================= DETAIL PAGE =================
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
# ================= ADD COMMENT =================
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

# ================= MY BOOKING PAGE =================
@login_required(login_url='login')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "apps/my_bookings.html", {
        "bookings": bookings
    })

@login_required(login_url='login')
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, id=pk, user=request.user)
    booking.delete()
    messages.success(request, "Booking cancelled successfully")
    return redirect('my_bookings')
    
# ================= contact us =================
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Your message has been sent successfully! we will contact u soon")
        return redirect('contact')  
    return render(request, 'apps/contact.html') 

# search cities or else navbar
from django.db.models import Q

def search(request):
    query = request.GET.get('q', '').strip().lower()

    treking_results = []
    camping_results = []
    caravan_results = []
    news_results = []

    if query:
        #  DIRECT TYPE SEARCH (FAST + SIMPLE)
        if "trek" in query:
            treking_results = Treking.objects.all()

        elif "camp" in query:
            camping_results = Camping.objects.all()

        elif "caravan" in query:
            caravan_results = Caravan.objects.all()
        else:
            #  GENERAL SEARCH (fallback)
            treking_results = Treking.objects.filter(
                Q(name__icontains=query) |
                Q(city__icontains=query) |
                Q(description__icontains=query) |
                Q(country__name__icontains=query)
            )
            camping_results = Camping.objects.filter(
                Q(namecamp__icontains=query) |
                Q(city__icontains=query) |
                Q(about__icontains=query) |
                Q(country__name__icontains=query)
            )

            caravan_results = Caravan.objects.filter(
                Q(name__icontains=query) |
                Q(city__icontains=query) |
                Q(description__icontains=query) |
                Q(country__name__icontains=query)
            )

            news_results = News.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query)
            )

    return render(request, "apps/search_results.html", {
        "query": query,
        "treking_results": treking_results,
        "camping_results": camping_results,
        "caravan_results": caravan_results,
        "news_results": news_results,
    })
# -------- API VIEWS --------

class trekingList(ListCreateAPIView):
    queryset = Treking.objects.all()
    serializer_class = TrekingSerializer

class trekingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Treking.objects.all()
    serializer_class = TrekingSerializer
   
# CAMPING API
class campingList(ListCreateAPIView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

class campingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Camping.objects.all()
    serializer_class = CampingSerializer

# CARAVN API
class caravanList(ListCreateAPIView):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer

class caravanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Caravan.objects.all()
    serializer_class = CaravanSerializer

# News API
class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# BOOKING API
class bookingCreate(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





