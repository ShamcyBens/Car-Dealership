from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create_car/', views.create_car, name='create_car'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('car_update/<int:car_id>/', views.update_car, name='car_update'),
    path('delete_car/<int:car_id>/', views.car_delete_profile, name='delete_car'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('profile', views.profile, name='profile'),

]