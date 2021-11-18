from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LogInForm, PostForm
from django.contrib import auth
from .models import Post
from django.http import Http404
from django.contrib import messages


# Create your views here.

def home(request):
    if 'name' in request.session:
        count = request.session.get('count', 0)
        new_count = count + 1
        request.session['count'] = new_count
        posts = Post.objects.all()
        context = {'posts': posts, 'count': new_count}
        response = render(request, 'home.html', context)
        response.set_cookie("name", "ovaixe", max_age=60)
        return response
    else:
        auth.logout(request)
        return redirect('logIn')


def signUp(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('logIn')
        else:
            return redirect('signUp')
            
    else:
        fm = UserCreationForm()
        context = {'form': fm}
        return render(request, 'signUp.html', context)


def logIn(request):
    if request.method == 'POST':
        fm = LogInForm(data=request.POST, request=request)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = auth.authenticate(username=uname, password=upass)
            if user is not None:
                auth.login(request, user)
                request.session['name'] = 'owais'
                request.session.set_expiry(0)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Username or Password!')
                return redirect('logIn')
        else:
            messages.info(request, 'Please input correct details!')
            return redirect('logIn')
    else:
        fm = LogInForm()
        context = {'form': fm}
        return render(request, 'logIn.html', context)


def logOut(request):
    auth.logout(request)
    return redirect('home')