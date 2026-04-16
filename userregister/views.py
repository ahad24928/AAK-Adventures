from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('login')

    
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
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		
		user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
		user.save();
		print('user created')
		return redirect('login')

	else:
		return render(request, 'userregister/register.html')





