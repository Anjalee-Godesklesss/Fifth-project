from django.shortcuts import render, import
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if request.method=='POST':
        first_name=rquest.POST('first_name')
        last_name=request.POST('last_name')
        username=request.POST('username')
        email=request.POST('email')
        password = request.POST('password')
        password2= request.POST('password2')

    #check if passwords match
    if password == password2:
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                auth.login(request, user)
                messages.success(request, 'you are now logged in')
                return redirect('index')
    else:
        messages.error(request, 'passwords do not match')
        return redirect('register')
    else:
        return render(request, 'accountssss/register.html')
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            message.success(request, 'you are logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
    else:
        return render(request, 'accountssss/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accountssss/dashboard.html')
