from django.shortcuts import render, HttpResponse, redirect
from models import *
  # the index function is called when root is visited
def index(request):
    return render(request, 'nip/login.html')



def new_user(request):
	errors = User.objects.regis_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	image = request.POST['picture']
	password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	User.objects.create(first_name=first_name, last_name=last_name, email=email, image=image,password=password)
	request.session['id'] = User.objects.get(email=email).id
	return redirect('/')

def login(request):
	errors = User.objects.log_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	email = request.POST['email']
	request.session['id'] = User.objects.get(email=email).id
	context = {
		'picture': User.objects.get(id=request.session['id']).image,
		'name': User.objects.get(id=request.session['id']).first_name
	}
	return render(request,'nip/home.html',context)


def strength(request):
    context = {
        'stacks': Stack.objects.all()
    }
    return render(request, 'nip/strengths.html', context)
    user = User.objects.get(id=request.session['id'])
    for id in request.POST.getlist['s.check']:
        user.strengths.add(id=id)

        
    