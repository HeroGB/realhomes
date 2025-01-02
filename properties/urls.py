# properties/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

app_name = 'properties'  # Define the app_name for the 'properties' app

# Create a DefaultRouter for managing properties
router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')

urlpatterns = [
    # Include all property-related routes from the router
    path('', include(router.urls)),
]
