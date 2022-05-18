"""Project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from django.contrib import admin
from django.urls import path
from argparse import Namespace
from xml.etree.ElementInclude import include
from Api.views import UserDetailAPI,RegisterUserAPIView
from rest_framework_simplejwt import views as jwt_views
from Api.views import TICKETAddAPIView, TICKETDeleteView, TICKETListView, TICKETUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("get-details",UserDetailAPI.as_view()),
    path('anand',RegisterUserAPIView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  
  # path('auth/', include('rest_framework.urls', Namespace='rest_framework'))
    path('Ticketlist/', TICKETListView.as_view()),
    path('Ticketadd/', TICKETAddAPIView.as_view()),
    path("Ticketupdate/<int:pk>", TICKETUpdateView.as_view()),
    path('Ticketdelete/<int:pk>', TICKETDeleteView.as_view()),
   
   

     
   # path('api-token-auth', views.obtain_auth_token)
]