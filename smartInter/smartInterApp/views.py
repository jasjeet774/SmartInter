from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect")
       
    return render(request,'login.html')

from django.db import IntegrityError

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if password!=confirmPassword:
            return HttpResponse("your password and confirm password are not same")
        else:
            # Check if the username is unique
            if User.objects.filter(username=username).exists():
            # Handle the case when the username is not unique
                return HttpResponse("Username is already taken. Please choose a different username.")

            try:
                my_user = User.objects.create_user(username, email, password)
                my_user.save()
                # return render(request,'login.html')
                return redirect('userlogin')
            except IntegrityError:
                # Handle other database integrity errors here if necessary
                return HttpResponse("An error occurred while creating the user.")

    return render(request, 'signup.html')

            


def home(request):
    return render(request,'home.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')