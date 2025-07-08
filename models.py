from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image=models.FileField(default=1)
    status = models.CharField(max_length=100, default="On Hold")

    class Meta:
        db_table = "Registration"


class Admin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Admin_login"


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Notifications"


class Speech(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    names = models.CharField(max_length=300)
    age = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=300)
    ethnicity = models.CharField(max_length=300)
    religion = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    nationality = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    speecher = models.CharField(max_length=300)
    speech = models.CharField(max_length=500)
    sdate = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=300)
    status = models.CharField(max_length=100)
    score=models.FloatField()

    class Meta:
        db_table = 'speech'

class SpeechModel(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    names = models.CharField(max_length=300)
    age = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=300)
    ethnicity = models.CharField(max_length=300)
    religion = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    nationality = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    speecher = models.CharField(max_length=300)
    speech = models.CharField(max_length=300)
    sdate = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=300)
    status = models.CharField(max_length=100)
    score=models.FloatField()

    class Meta:
        db_table = 'speech_model'