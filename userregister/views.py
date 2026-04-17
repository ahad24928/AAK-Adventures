from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')

    
def login(request):
	if request.method== 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'invalid login details')
			return redirect('login')
	else:
		return render(request, 'userregister/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'userregister/register.html')


@api_view(['POST'])
def register_api(request):
    data = request.data

    if data['password'] != data.get('confirm_password'):
        return Response({"error": "Passwords do not match"}, status=400)

    if User.objects.filter(username=data['username']).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        email=data.get('email')
    )

    return Response({"message": "User created successfully"}, status=201)





