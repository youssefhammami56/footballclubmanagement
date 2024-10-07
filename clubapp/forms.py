from imaplib import _Authenticator
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Notification
from .models import Competition



from clubapp.models import Player
from django import forms
from .models import Player

class JoinPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'nationality', 'birth_date']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'content']

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'date', 'location']
        
        
       

