# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from igames.models import *
from django.core import serializers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from sets import Set
from igames.forms import *
import json
import os.path

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Games aPP',
		'pagetitle': 'Welcome to the Games aPPlication',
		'contentbody': 'Managing the development of games since 2014',
		'user': request.user,
		})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, username, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')

	if not fm:
		games = Game.objects.filter(developers=user)
		platforms = Set([])
		companies = Set([])
		for game in games:
			companies.add(game.company)
			for platform in game.platforms.all():
				platforms.add(platform)
	
		template = get_template('userpage.html')
		variables = Context({
			'user': user,
			'games': games,
			'platforms': platforms,
			'companies': companies,
		
			})
		output = template.render(variables)
		return HttpResponse(output)

	elif fm == ".xml":
		data = serializers.serialize("xml",User.objects.filter(username=username))
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",User.objects.filter(username=username))
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.') 

def userspage(request, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')

	if not fm:	
		template = get_template('generalpage.html')
		developers = User.objects.all()
		variables = Context({
			'title': 'Developers',
			'vars': developers,
			'link': 'developers',
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",User.objects.all())
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",User.objects.all())
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def gamepage(request, gamename,fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	try:
		game = Game.objects.get(name=gamename)
	except:
		raise Http404('Game not found.')

	if not fm:
		template = get_template('gamepage.html')
		owner = False
		if request.user.is_staff:
			owner = True
		else:
			for developer in game.developers.all():
				if developer.username == request.user.username:
					owner = True
		
		variables = Context({
			'game': game,
			'owner': owner,
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",Game.objects.filter(name=gamename))
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Game.objects.filter(name=gamename))
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def gamespage(request, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	if not fm:
		template = get_template('generalpage.html')
		games = Game.objects.all()
		variables = Context({
			'title': 'Games',
			'vars': games,
			'link': 'games',
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",Game.objects.all())
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Game.objects.all())
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def companypage(request, companyname, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	try:
		company = Company.objects.get(name=companyname)
		games = Game.objects.filter(company=company)
	except:
		raise Http404('Company not found.')

	if not fm:
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
	elif fm == ".xml":
		data = serializers.serialize("xml",Company.objects.all())
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Company.objects.all())
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def companiespage(request, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	if not fm:	
		template = get_template('generalpage.html')
		companies = Company.objects.all()
		variables = Context({
			'title': 'Companies',
			'vars': companies,
			'link': 'companies',
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",Company.objects.all())
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Company.objects.all())
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def platformpage(request, platformname,fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	try:
		platform = Platform.objects.get(name=platformname)
		games = Game.objects.filter(platforms=platform)
	except:
		raise Http404('Platform not found.')

	if not fm:
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
	elif fm == ".xml":
		data = serializers.serialize("xml",Platform.objects.filter(name=platformname))
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Platform.objects.filter(name=platformname))
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def platformspage(request,fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	if not fm:
		template = get_template('generalpage.html')
		platforms = Platform.objects.all()
		variables = Context({
			'title': 'Platforms',
			'vars': platforms,
			'link': 'platforms',
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",Platform.objects.all())
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Platform.objects.all())
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login")
    else:
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

class GameCreate(CreateView):
	model = Game
	template_name = 'formcreate.html'
	form_class = GameForm

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(GameCreate,self).form_valid(form)

def mygamespage(request, fm):
	if not request.user.is_authenticated():
        	return redirect('/login')
	try:
		user = User.objects.get(username=request.user.username)
	except:
		raise Http404('User not found.')

	if not fm:
		template = get_template('generalpage.html')
		games = Game.objects.filter(developers=user)
		variables = Context({
			'title': 'Games',
			'vars': games,
			'link': 'games',
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif fm == ".xml":
		data = serializers.serialize("xml",Game.objects.filter(developers=user))
		return HttpResponse(data, mimetype="application/xml")
	elif fm == '.json':
		data = serializers.serialize("json",Game.objects.filter(developers=user))
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404('Page not found.')

def resources(request, resource):
	os.path.join(os.path.dirname(__file__),'/templates/resources')
	if resource == "countries.json":
		
		json_data=open(os.path.join(os.path.dirname(__file__),'./templates/resources/countries.json'))
		data=json.loads(json_data)
		
		print (data)
		#data2=json.dumps(json_data)
		json_data.close()

		return HttpResponse(data, mimetype="application/json")
