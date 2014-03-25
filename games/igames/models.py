from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	name = models.TextField(max_length = 100)
	fundation_date = models.DateTimeField()

	def __unicode__(self):
		return self.name
	
class Platform(models.Model):
	name = models.TextField(max_length = 100)

	def __unicode__(self):
		return self.name

class Game(models.Model):
	name = models.TextField(max_length = 20)
	release_date = models.DateTimeField()
	price = models.IntegerField()
	description = models.TextField(max_length = 100)
	
	developers = models.ManyToManyField(User)
	company = models.ForeignKey(Company)
	platforms = models.ManyToManyField(Platform)
	
	def __unicode__(self):
		return "Name: "+self.name + ", Company: " + self.company.name

	
