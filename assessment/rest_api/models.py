from django.db import models

# Create your models here.

APPOINTMENT_KIND_CHOICES = [
    ('NP', 'New Patient'),
    ('FU', 'Follow-up')
]

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadata"""

        abstract = True

class Doctor(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"

class Appointment(BaseModel):
    patient_first_name = models.CharField(max_length=255)
    patient_last_name = models.CharField(max_length=255)
    kind = models.CharField(
        max_length=3,
        choices=APPOINTMENT_KIND_CHOICES,
        default='NP'
    )
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE,
        related_name='appointments'
    )

    def __str__(self):
        return f"patient: {self.patient_first_name} -> doctor: {self.doctor} -> date: {self.appointment_date}"
