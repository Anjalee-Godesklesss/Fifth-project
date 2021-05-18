from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        message.error(requets, 'Testing error message')
           return redirect('register')
    else:
        return render(request, 'accountssss/register.html')
# Create your views here.

def login(request):
    return render(request, 'accountssss/login.html')


def dashboard(request):
    return render(request, 'accountssss/dashboard.html')


def logout(request):
    return redirect('index')