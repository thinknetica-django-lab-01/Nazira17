"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main import views
from main.views import *
urlpatterns = [
    path('', views.home),
    path('goods/', ProductList.as_view(), name="product"),
    path('goods/add/', ProductCreateView.as_view(), name="product_add"),
    path('goods/<int:pk>/edit/', ProductUpdateView.as_view(), name="product_edit"),
    path('goods/<int:id>', ProductDetailView.as_view(), name="product_detail"),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/profile/', CustomerUpdate.as_view(), name='customer-update'),
    path('accounts/', include('allauth.urls')),
    path('subscriber/', subscribe_user, name='subscriber'),
]
