from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Owner, Customer

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
        user = auth.authenticate(request, username = userid, password = userpwd)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request, 'login.html') 

def logout(request):
    auth.logout(request)
    return redirect('home')

def divide(request, user_id):
    if request.user.profile.belong == 1:
        return redirect('home')

    elif request.user.profile.belong == 0:
        user = User.objects.get(pk = user_id)
        owner = Owner()
        owner.id = user
        owner.save()
        return redirect('home')
    