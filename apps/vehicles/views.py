from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Automatically assign the owner to the logged-in user
        serializer.save(owner=self.request.user)
