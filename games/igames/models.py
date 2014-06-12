from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

def get_default_user():
    return User.objects.get(pk=1)

class Company(models.Model):
	name = models.TextField(max_length = 20)
	fundation_date = models.DateTimeField()
	city = models.TextField(max_length = 20)
	stateOrProvince = models.TextField(max_length = 20)
	country = models.TextField(max_length = 20)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('company-detail', kwargs={'name': self.name})
	
class Platform(models.Model):
	name = models.TextField(max_length = 20)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('platform-detail', kwargs={'name': self.name})

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
	def get_absolute_url(self):
		return reverse('game-detail', kwargs={'name': self.name})
	def averageRating(self):
		ratingSum = 0.0
		for review in self.gamereview_set.all():
		    ratingSum += review.rating
		reviewCount = self.gamereview_set.count()
		return ratingSum / reviewCount

	
class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=get_default_user)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class GameReview(Review):
    game = models.ForeignKey(Game)


