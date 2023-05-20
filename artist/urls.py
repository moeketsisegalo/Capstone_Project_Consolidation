from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Define the URL patterns

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Albums page
    path('albums/', views.albums, name='albums'),

    # Tour page
    path('tours/', views.tour, name='tours'),

    # User registration page
    path('register/', views.register, name='register'),

    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
