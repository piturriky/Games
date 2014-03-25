# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from igames.models import *

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Games aPP',
		'pagetitle': 'Welcome to the Games aPPlication',
		'contentbody': 'Managing the development of games since 2014'
		})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	games = user.game_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'games': games
		})
	output = template.render(variables)
	return HttpResponse(output)

def companiespage(request):
	template = get_template('generalpage.html')
	companies = Company.objects.all()
	variables = Context({
		'title': 'Companies',
		'vars': companies,
		})
	output = template.render(variables)
	return HttpResponse(output)

def gamespage(request):
	template = get_template('generalpage.html')
	games = Game.objects.all()
	variables = Context({
		'title': 'Games',
		'vars': games,
		})
	output = template.render(variables)
	return HttpResponse(output)

def platformspage(request):
	template = get_template('generalpage.html')
	platforms = Platform.objects.all()
	variables = Context({
		'title': 'Platforms',
		'vars': platforms,
		})
	output = template.render(variables)
	return HttpResponse(output)

def companypage(request, companyname):
	try:
		company = Company.objects.get(name=companyname)
	except:
		raise Http404('Company not found.')

	template = get_template('companypage.html')
	variables = Context({
		'company': company,
		})
	output = template.render(variables)
	return HttpResponse(output)

def gamepage(request, gamename):
	try:
		game = Game.objects.get(name=gamename)
	except:
		raise Http404('Game not found.')

	template = get_template('gamepage.html')

	variables = Context({
		'game': game,
		})
	output = template.render(variables)
	return HttpResponse(output)

def platformpage(request, platformname):
	try:
		platform = Platform.objects.get(name=platformname)
	except:
		raise Http404('Platform not found.')

	template = get_template('platformpage.html')
	variables = Context({
		'platform': platform,
		})
	output = template.render(variables)
	return HttpResponse(output)

