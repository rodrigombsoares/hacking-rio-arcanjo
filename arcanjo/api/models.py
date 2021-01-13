from django.db import models


class Session(models.Model):
    phone_number = models.CharField(max_length=14)
    guardian_name = models.CharField(
        max_length=200, 
        default=None,
        blank=True,
        null=True
    )
    ts_opening = models.DateTimeField(auto_now_add=True)
    ts_checkin = models.DateTimeField(
        default=None,
        blank=True,
        null=True
    )
    ts_sorting = models.DateTimeField(
        default=None,
        blank=True,
        null=True
    )
    ts_consultation_start = models.DateTimeField(
        default=None,
        blank=True,
        null=True
    )
    ts_consultation_end = models.DateTimeField(
        default=None,
        blank=True,
        null=True
    )


class Patient(models.Model):
    cpf = models.CharField(max_length=200)
    name = models.CharField(
        max_length=200,
        default=None,
        blank=True,
        null=True
    )
    insurance_number =  models.CharField(
        max_length=200,
        default=None,
        blank=True,
        null=True
    )


class PatientSymptom(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        default = None
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=300)


class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    step = models.IntegerField(default=0)
    sid = models.CharField(max_length=300, default=None)


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Specialty(models.Model):
    name = models.CharField(max_length=200)
    session = models.ForeignKey(Hospital, on_delete=models.CASCADE)