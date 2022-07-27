from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from models import Profile
# from .models import User_owner, User_customer, Profile

def register_owner(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            name = request.POST['name']
            number = request.POST['number']
            belong = 0
            user_owner = Profile(user=user, name=name, number=number, belong=belong)
            user_owner.save()
            auth.login(request,user)
            return redirect('home')
    return render(request, 'register_owner.html') 
    
def register_customer(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            name = request.POST['name']
            number = request.POST['number']
            belong = 1
            user_customer = Profile(user=user, name=name, number=number, belong=belong)
            user_customer.save()
            auth.login(request,user)
            return redirect('home')
    return render(request, 'register_customer.html') 



def login(request):
    if request.method == 'POST':
        
        userid = request.POST['username']
        userpwd = request.POST['password']
        userType = request.POST['type']
        print(request.POST)
        user = auth.authenticate(request, username = userid, password = userpwd)
        if userid=="admin@admin.com" and userpwd=="1234":
            #auth.login(request,user)
            if userType=="customer":
                return redirect('signin')
            return redirect('signIn.html')
        else : 
            print("here") 
            return render(request, 'login.html',{'isLogin': "false"})

    else:
        return render(request, 'login.html') 

def signUp(request):
    if request.method == 'POST':
        return render(request, 'login.html',{'isLogin': "false"})
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
