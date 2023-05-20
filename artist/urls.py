from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    """
    The home page URL pattern.
    
    :param: None
    :type: None
    :return: The rendered home page.
    :rtype: HttpResponse
    """

    path('albums/', views.albums, name='albums'),
    """
    The albums page URL pattern.
    
    :param: None
    :type: None
    :return: The rendered albums page.
    :rtype: HttpResponse
    """

    path('tours/', views.tour, name='tours'),
    """
    The tours page URL pattern.
    
    :param: None
    :type: None
    :return: The rendered tours page.
    :rtype: HttpResponse
    """

    path('register/', views.register, name='register'),
    """
    The user registration page URL pattern.
    
    :param: None
    :type: None
    :return: The rendered user registration page.
    :rtype: HttpResponse
    """

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    """
    The login page URL pattern.
    
    :param: template_name: The template to use for rendering the login page.
    :type: str
    :return: The rendered login page.
    :rtype: HttpResponse
    """

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    """
    The logout page URL pattern.
    
    :param: None
    :type: None
    :return: The rendered logout page.
    :rtype: HttpResponse
    """
]
