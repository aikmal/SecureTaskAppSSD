from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # The home page
    path('', views.home, name='home'),
    
    # Secure Login/Logout (Django handles the logic automatically!)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Registration
    path('register/', views.register, name='register'),
    
    # The Main Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Task Actions
    path('create-task/', views.create_task, name='create_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
]