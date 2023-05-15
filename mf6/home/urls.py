
from django.contrib import admin
from django.urls import path, include, re_path
#check this part
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import LoginView, SignupView
from mf6.home import views
#import members.urls

urlpatterns = [

    # The home page
    path('',views.Index.as_view(),name='mf6-home'),
    path('projectadd',views.AddProject.as_view(),name='project-add'),
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='mf6pages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
