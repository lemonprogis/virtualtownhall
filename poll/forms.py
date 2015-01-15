from django import forms
from django.forms import ModelForm
from models import *

class TownHallPollForm(ModelForm):
	class Meta:
		model = TownHallPoll
		fields = ["question"]

class TownHallResponseForm(ModelForm):
	first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	email =forms.CharField(required=False, widget=forms.EmailInput(attrs={'class':'form-control'}))
	answer = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
	class Meta:
		model = TownHallResponse
		fields = ["first_name", "last_name", "email", "answer","poll"]