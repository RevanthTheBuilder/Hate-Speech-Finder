from django import forms
from .models import *


class NotificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        exclude = ["date_time"]


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ["status"]


class SpeechForm(forms.ModelForm):
    class Meta:
        model = Speech
        exclude = ['status','sdate','score']
