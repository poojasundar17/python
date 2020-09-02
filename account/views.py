from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  User,auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
#from django.contrib.auth.forms import UserCreationForm



# Create your views here.'''
def login(request):
	if request.method == 'POST':
		username =request.POST['username']
		password = request.POST['password']
		
		
		user = auth.authenticate(username=username,password=password)
		
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'invalid user')
			return redirect('login')
	else:
		return render(request,'main/login.html')


def register(request):
	if request.method == 'POST':
		
		username=request.POST['username']
		email =request.POST['email']
		password1 = request.POST['password1']
		password2 =request.POST['password2']
		#gender =request.POST['gender']
		
		
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username already exits')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email is already exits')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,email=email,password=password1)
				user.save();
				print('user created')
				return redirect('/')
		else:
			messages.info(request,'Password not matching')
			return redirect('register')
		return redirect('main:homepage')
	else:
		return render(request,'main/register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
	



