from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.post['username']
        password=request.POST['password']
        x =auth.authenticate(username=username, password=password)
        if x is None:
            return redirect('login')
        else:
            return redirect('/')
    else:
        return render(request, 'login.html')