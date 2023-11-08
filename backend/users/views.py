from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def userlogin(request):
    page='login'
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print('User does not exist')
        user=authenticate(User, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/')
        else:
            print('username or password incorrect')
    return render(request,'user-login.html')

def userlogout(request):
    logout(request)
    return redirect('login')

def userregister(request):
    page='register'
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
    context={'page':page, 'form':form}
    return render(request, 'user-login.html', context)
