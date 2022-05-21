from django.urls import reverse
from rest_api.serializers import AppointmentSerializer, DoctorSerializer
from rest_framework.test import APITestCase, APIClient

# VIEWS
class WelcomeTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.get_welcome_url = reverse('welcome')

    def test_welcome_endpoint_returns_successful(self):
        """
        Should return HTTP 200 when get request sent to welcome endpoint
        """

        response = self.client.get(self.get_welcome_url)
        self.assertEqual(response.status_code, 200)


class DoctorTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        

class AppointmentTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.get_appointment_url = reverse('appointment-list')


    def test_same_time_appointment_should_not_be_created_when_doctor_already_has_three_appointment(self):

        doctor = {
                "first_name": "test",
                "last_name": "test"
        }
        doctor_serializer = DoctorSerializer(data=doctor)
        doctor_serializer.is_valid(raise_exception=True)
        doctor_serializer.save()

        appointment = {
                "patient_first_name": "string",
                "patient_last_name": "string",
                "kind": "NP",
                "appointment_date": "2022-05-23T15:45:45.000Z",
                "doctor": 1
        }
        appointment_serializer = AppointmentSerializer(data=appointment)
        appointment_serializer.is_valid(raise_exception=True)
        appointment_serializer.save()
           
        self.client.post(
            self.get_appointment_url, {
                "patient_first_name": "string",
                "patient_last_name": "string",
                "kind": "NP",
                "appointment_date": "2022-05-23T15:45:45.000Z",
                "doctor": 1
            }
        )
        self.client.post(
            self.get_appointment_url, {
                "patient_first_name": "string",
                "patient_last_name": "string",
                "kind": "NP",
                "appointment_date": "2022-05-23T15:45:45.000Z",
                "doctor": 1
            }
        )
        self.client.post(
            self.get_appointment_url, {
                "patient_first_name": "string",
                "patient_last_name": "string",
                "kind": "NP",
                "appointment_date": "2022-05-23T15:45:45.000Z",
                "doctor": 1
            }
        )

        response = self.client.post(
            self.get_appointment_url, appointment
        )
        self.assertEqual(response.status_code, 400)
