from django.db import models

class TownHallPoll(models.Model):
	question = models.CharField(max_length=255)
	is_published = models.BooleanField(default=False, verbose_name='published')
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.question

	def __str__(self):
		return self.question

class TownHallResponse(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	answer = models.TextField()
	poll = models.ForeignKey(TownHallPoll)
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.answer

	def __str__(self):
		return self.answer
