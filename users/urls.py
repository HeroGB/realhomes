from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
