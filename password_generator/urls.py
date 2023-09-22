from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    # Define your URL patterns here
    path('', views.password_generation_page, name='password_generation_page'),
    ]
