# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

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
