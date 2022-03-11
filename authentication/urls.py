from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="index"),

    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]
