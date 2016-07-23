from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.utils import timezone
import datetime
# User methods*****************************************************************************************
def direct(request):
	return redirect( 'main/')
def main(request):
	now = datetime.datetime.now()
	time = str(now.strftime("%Y-%m-%d"))
	print time
	try:
		request.session['messages']
	except:
		request.session['messages'] = None
	todaysDate = timezone.now()

	if request.session['messages']:
		context = {
		'registerMessages': request.session['messages'],
		'time' : time
		}
		del request.session['messages']
		return render(request, 'logreg/main.html', context)
	else:
		context = {
		'time': time
		}
		return render(request, 'logreg/main.html', context)

def register(request):

	password = request.POST['password']
	if request.POST['password'] != request.POST['confirmPass']:
		request.session['messages'] ='Passwords dont match!'
		return redirect('/main/')
	elif len(request.POST['password']) < 8:
		request.session['messages'] ='Passwords not long enough. Must be eight characters!'
		return redirect('/main')
	elif len(request.POST['name']) < 3 or len(request.POST['username']) < 3:
		request.session['messages'] ='Username and name must be at least 3 letters long!'
		return redirect('/main/')
	elif len(request.POST['birthdate']) < 4:
		request.session['messages'] ='Please fill out birthdate.'
		return redirect('/main/')
	elif len(request.POST['email']) < 4:
		request.session['messages'] ='Please fill out email. must be longer then 4'
		return redirect('/main/')
	else:

		userCount = User.objects.filter(username = request.POST['username']).count()
		if userCount > 0:
			request.session['messages'] ='User already exists! Try another username.'
			return redirect('/main/')
		else:
			name = request.POST['name']
			username = request.POST['username']
			email = request.POST['email']
			password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
			birthdate = request.POST['birthdate']
			user =  User.objects.create(name = name, username = username, email=email, password = password, birthdate = birthdate)
			request.session['messages'] ='User created.'
			return redirect('/main/')

def login(request):
		userCount = User.objects.filter(username = request.POST['usernameLogin']).count()
		if userCount <1:
			request.session['messages'] = 'No user found/password not correct.'
			return redirect('/main/')
		else:
			storedUser = User.objects.get(username = request.POST['usernameLogin'])
			testpw = bcrypt.hashpw(request.POST['passwordLogin'].encode('utf-8'), storedUser.password.encode('utf-8'))
			if testpw != storedUser.password:
				request.session['messages'] = 'No user found/password not correct.'
				return redirect('/main/')
			else:
				request.session['userId'] = storedUser.id
				request.session['userName'] = storedUser.name
				request.session['user_userName'] = storedUser.username
				return redirect('/pokes/')

def logout(request):
	try: 
		request.session['userName']

	except:
		return redirect('/main/')
	del request.session['userId']
	del request.session['userName']
	del request.session['user_userName']
	request.session['messages'] = 'logged out.'
	return redirect('/main')



	


	




	


	