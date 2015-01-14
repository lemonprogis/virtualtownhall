from django.forms import ModelForm
from models import *

class TownHallPollForm(ModelForm):
	class Meta:
		model = TownHallPoll
		fields = ["question"]

class TownHallResponseForm(ModelForm):
	class Meta:
		model = TownHallResponse
		fields = ["first_name", "last_name", "email", "answer","poll"]