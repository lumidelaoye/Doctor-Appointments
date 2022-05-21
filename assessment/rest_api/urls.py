from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_api.views import (
    WelcomeView, 
    DoctorViewSet, 
    AppointmentViewSet
)

schema_view = get_schema_view(
   openapi.Info(
      title="Doctor's appointment Manager",
      default_version='v1',
      description="Doctor's Appointment Manager API",
      contact=openapi.Contact(email="lumidelaoye22@gmail.com")
   ),
   public=True
)

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'appointment', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path(r'', include(router.urls)),
    path("welcome", WelcomeView.as_view(), name="welcome"),
    path(
        'swagger',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]