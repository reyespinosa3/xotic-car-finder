from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:car_id>/', views.onecar, name='onecar'),
	path('post_url/', views.post_car, name='post_car'),
	path('user/<username>/', views.profile, name='profile'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('buyersignup/', views.buyersignup_view, name='buyersignup'),
	path('sellersignup/', views.sellersignup_view, name='sellersignup'),
]
