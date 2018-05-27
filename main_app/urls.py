from django.conf.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:car_id>/', views.onecar, name='onecar'),
	path('post_url/', views.post_car, name='post_car')
]
