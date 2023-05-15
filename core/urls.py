# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this
from core import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # The admin and accounts page
    path('admin/', admin.site.urls),          # Django admin route
    path("accounts/", include('allauth.urls')),
    #path('accounts/logouts/', views.KeycloakLogoutView.as_view(), name='account_logouts'),
    # ADD NEW Routes HERE
    path("mf6/", include("mf6.home.urls")),    
    # path("tupacviewer/", include("tupacviewer.urls"))
]
