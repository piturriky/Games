# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from igames.models import *

from sets import Set

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
	games = Game.objects.filter(developers=user)

	platforms = Set([])
	companies = Set([])
	for game in games:
		companies.add(game.company)
		for platform in game.platforms.all():
			platforms.add(platform)
	
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'games': games,
		'platforms': platforms,
		'companies': companies,
		
		})
	output = template.render(variables)
	return HttpResponse(output)

def companiespage(request):
	template = get_template('generalpage.html')
	companies = Company.objects.all()
	variables = Context({
		'title': 'Companies',
		'vars': companies,
		'link': 'companies',
		})
	output = template.render(variables)
	return HttpResponse(output)

def gamespage(request):
	template = get_template('generalpage.html')
	games = Game.objects.all()
	variables = Context({
		'title': 'Games',
		'vars': games,
		'link': 'games',
		})
	output = template.render(variables)
	return HttpResponse(output)

def platformspage(request):
	template = get_template('generalpage.html')
	platforms = Platform.objects.all()
	variables = Context({
		'title': 'Platforms',
		'vars': platforms,
		'link': 'platforms',
		})
	output = template.render(variables)
	return HttpResponse(output)

def userspage(request):
	template = get_template('generalpage.html')
	developers = User.objects.all()
	variables = Context({
		'title': 'Developers',
		'vars': developers,
		'link': 'developers',
		})
	output = template.render(variables)
	return HttpResponse(output)

def companypage(request, companyname):
	try:
		company = Company.objects.get(name=companyname)
		games = Game.objects.filter(company=company)
	except:
		raise Http404('Company not found.')

	developers = Set([])
	platforms = Set([])
	for game in games:
		for platform in game.platforms.all():
			platforms.add(platform)
		for developer in game.developers.all():
			developers.add(developer)

	template = get_template('companypage.html')
	variables = Context({
		'company': company,
		'games':games,
		'platforms': platforms,
		'developers':developers,
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
		games = Game.objects.filter(platforms=platform)
	except:
		raise Http404('Platform not found.')

	developers = Set([])
	companies = Set([])
	for game in games:
		companies.add(game.company)
		for developer in game.developers.all():
			developers.add(developer)

	template = get_template('platformpage.html')
	variables = Context({
		'platform': platform,
		'games':games,
		'companies': companies,
		'developers':developers,
		})
	output = template.render(variables)
	return HttpResponse(output)


