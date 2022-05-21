from datetime import datetime
from rest_framework import serializers
from rest_api.models import Doctor, Appointment
from django.db.models import Q

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    def validate_appointment_date(self, appointment_date):
        if appointment_date.replace(tzinfo=None) <= datetime.now():
            raise serializers.ValidationError(
                "appointment_date must be in the future"
            )
        
        appointment_date_in_minute = appointment_date.minute
        if appointment_date_in_minute % 15 != 0:
            raise serializers.ValidationError(
                "appointment_date must be in 15 minutes interval"
            )
            
        doctor_id = self.initial_data['doctor']
        similar_appointments = Appointment.objects.filter(
            Q(appointment_date=appointment_date) &
            Q(doctor__id = doctor_id)
        )
        print(similar_appointments)

        if len(similar_appointments) > 3:
            raise serializers.ValidationError(
                "3 appointments with the same time already exists for this doctor"
            )        
        
        return appointment_date.replace(tzinfo=None)

    class Meta:
        model = Appointment
        fields = '__all__'
