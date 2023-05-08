"""defines the URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #include defalt auth urls.
    path('', include('django.contrib.auth.urls')),
    #registration view.
    path('register/', views.register, name='register'),
]