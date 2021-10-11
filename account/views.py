from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User, auth
from .models import *

userMessage = ""
username= ""

# Create your views here.
def home(request):
	return render(request, 'index.html')

def signupPatient(request):
	if request.method == 'POST':
		form = hospitalForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			data = form.cleaned_data
			username = data['username']
			password = data['password']
			confirm_password = data['confirm_password']
			email = data['email_id']
			first_name = data['first_name']
			last_name = data['last_name']

			if(password == confirm_password):
				user = User.objects.create_user(username=username,
  					password=password, email=email, first_name=first_name,
  					last_name=last_name)
				user.save()
				message="Account creation successfull. Kindly login!"
				return render(request, 'loginPatientForm.html', {'message': message})
			else:
				message="Password and Confirm Password field does not match. Account creation faied!"
				return render(request, 'index.html', {'message': message})
	else:
		form = hospitalForm()
		return render(request, 'signupPatientForm.html', {'form' : form})

def loginPatient(request):
	if request.method == 'POST':
		global username, userMessage
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			if user.is_staff == True:
				message="Staff login not allowed from here"
				return render(request, 'loginPatientForm.html', {'message': message})
			else:
				userMessage = "Welcome patient,"
				return redirect('account:dashboardShow')
		else:
			message="Invalid email or password"
	return render(request, 'loginPatientForm.html')

def dashboardShow(request):
	global username, userMessage
	user = formHospital.objects.get(username=username)
	return render(request, 'dashboard.html', {'user': user, 'userMessage': userMessage})

def success(request):
	message="Account creation successfull. Kindly login!"
	return render(request, 'loginForm.html', {'message': message})

def signupDoctor(request):
	if request.method == 'POST':
		form = hospitalForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			data = form.cleaned_data
			username = data['username']
			password = data['password']
			confirm_password = data['confirm_password']
			email = data['email_id']
			first_name = data['first_name']
			last_name = data['last_name']

			if(password == confirm_password):
				user = User.objects.create_user(username=username,
	  				password=password, email=email, first_name=first_name,
	  				last_name=last_name, is_staff=True)
				user.save()
				message="Account creation successfull. Kindly login!"
				return render(request, 'loginDoctorForm.html', {'message': message})
			else:
				message="Password and Confirm Password field does not match. Account creation failed!"
				return render(request, 'index.html', {'message': message})
	else:
		form = hospitalForm()
		return render(request, 'signupDoctorForm.html', {'form' : form})

def loginDoctor(request):
	if request.method == 'POST':
		global username, userMessage
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			if user.is_staff == False:
				message="Patient login not allowed from here"
				return render(request, 'loginDoctorForm.html', {'message': message})
			else:
				userMessage = "Welcome Doctor,"
				return redirect('account:dashboardShow')
		else:
			message="Invalid email or password"
			return render(request, 'loginDoctorForm.html', {'message': message})
	else:
		return render(request, 'loginDoctorForm.html')


def logout(request):
	auth.logout(request)
	return redirect('account:home')