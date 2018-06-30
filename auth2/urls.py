from django.urls import path, include
from . import views



urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
]