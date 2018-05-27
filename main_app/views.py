from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car
from .forms import CarForm


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
		car.save()
	return HttpResponseRedirect('/')
