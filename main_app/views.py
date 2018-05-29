from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car
from .forms import CarForm, LoginForm


# Homepage view
def index(request):
	cars = Car.objects.all()
	form = CarForm()
	return render(request, 'index.html', { 'cars':cars, 'form':form })


# Individual car view
def onecar(request, car_id):
	car = Car.objects.get(id=car_id)
	return render(request, 'onecar.html', { 'car':car })


# Seller post car information
def post_car(request):
	form = CarForm(request.POST)
	if form.is_valid:
		car = form.save(commit = False)
		car.user = request.user
		car.save()
	return HttpResponseRedirect('/')


# User Profile
def profile(request, username):
	user = User.objects.get(username=username)
	cars = Car.objects.filter(user=user)
	return render(request, 'profile.html', {'username': username, 'cars': cars})


# Signup page view
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

# Login page view
def login_view(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print("user is active")
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
                return HttpResponse('/')
            else:
                print("The username and/or password is incorrect.")
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



# Log out view
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
