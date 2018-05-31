from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Car
from .forms import CarForm, LoginForm


# Homepage view
def index(request):
	cars = Car.objects.all()
	return render(request, 'index.html', { 'cars':cars })

# Show all cars view
def show(request):
	cars = Car.objects.all()
	return render(request, 'show.html', { 'cars':cars })

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
	return HttpResponseRedirect('/show')
	# return render(request, 'show.html', { 'username': username, 'cars': cars })


# User Profile
def profile(request, username):
	user = User.objects.get(username=username)
	cars = Car.objects.filter(user=user)
	form = CarForm()
	return render(request, 'profile.html', { 'username': username, 'form':form, 'cars': cars })





# Signup page view
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			my_group = Group.objects.get(name='seller')
			my_group.user_set.add(user)
			return HttpResponseRedirect('/show')
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
                    return HttpResponseRedirect('/show')
                else:
                    print("The account has been disabled.")
                return HttpResponseRedirect('/')
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
