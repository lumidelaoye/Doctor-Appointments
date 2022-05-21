from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_api.models import Doctor, Appointment
from rest_api.serializers import (
    DoctorSerializer, 
    AppointmentSerializer
)

class WelcomeView(APIView):
    """Welcome view just to ensure the server is running fine"""

    def get(self, request):
        """
            Get request for the welcome view
        """
        _ = request
        return Response({"message": "welcome"}, status=status.HTTP_200_OK)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
