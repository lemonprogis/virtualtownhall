from django.shortcuts import render
from django.http import HttpResponse
import json
from models import *
from forms import *

def post_answer(request):
	if request.method == 'POST':
		form = TownHallResponseForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse(json.dumps({'response':'Thanks for taking the time to answer!'}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'response':'no-data'}), content_type="application/json")

def view_polls(request):
	polls = TownHallPoll.objects.filter(is_published=True)
	form = TownHallResponseForm()

	return render(request, 'poll.html', {"polls": polls, "form":form,})