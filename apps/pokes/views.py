from django.shortcuts import render, redirect
from .models import User, Poke

def index(request):
	try:
		request.session['userId']
	except:
		return redirect('/')

	users = User.objects.all()
	context ={
		'othersInfo': [

		],
		'currentUser': {'name': request.session['userName'], 'id': request.session['userId'],
		 'username': request.session['user_userName'] ,
		 'poke_count': 0,
		 'poke_info': []
		 }
	}

	for user in users:
		if user.id != request.session['userId']:
			context['othersInfo'].append({'id': user.id, 'name': user.name,  'username': user.username, 'email': user.email, 'poke_count': Poke.objects.filter(user_poked = user.id).count()})
	for user in users:
		print user.name
		count = Poke.objects.filter(poked_by = user.id, user_poked= request.session['userId']).count()
		print count
		if count > 0:
			context['currentUser']['poke_count'] += count
			context['currentUser']['poke_info'].append({'name': user.name, 'poke_count': count})
	return render(request, 'pokes/index.html', context)

def addPoke(request, id):
	try:
		request.session['userId']
	except:
		return redirect('/')
	pokedUser  = User.objects.get(id = id)
	poker  = User.objects.get(id = request.session['userId'])
	poke = Poke.objects.create(user_poked= pokedUser, poked_by = poker)
	poke.save()
	return redirect('/pokes/')












