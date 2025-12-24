from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Optional: user viewset (admin-only, read-only)
from .views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    # User list (admin only)
    path('', include(router.urls)),

    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('apps.users.urls')),

]
