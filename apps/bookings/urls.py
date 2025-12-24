from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')  # include a prefix

urlpatterns = [
    path('', include(router.urls)),
]
