from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	name = models.TextField(max_length = 20)
	fundation_date = models.DateTimeField()
	stateOrProvince = models.TextField(max_length = 20)
	country = models.TextField(max_length = 20)

	def __unicode__(self):
		return self.name
	
class Platform(models.Model):
	name = models.TextField(max_length = 20)

	def __unicode__(self):
		return self.name

class Game(models.Model):
	name = models.TextField(max_length = 20)
	release_date = models.DateTimeField()
	price = models.IntegerField()
	genre = models.TextField(max_length = 20)
	description = models.TextField(max_length = 100)
	
	developers = models.ManyToManyField(User)
	company = models.ForeignKey(Company)
	platforms = models.ManyToManyField(Platform)
	
	def __unicode__(self):
		return "Name: "+self.name

	
