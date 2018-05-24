from django.shortcuts import render
from django.http import HttpResponse


# Index view to ensure all is working properly.
# def index(request):
# 	return HttpResponse('<h1>Hello World! Your Django App is Working!</h1>')

def index(request):
	return render(request, 'index.html')
