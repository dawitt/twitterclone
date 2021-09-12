from django.http.response import HttpResponseRedirect
from authentication.forms import LoginForm, SignupForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from twitteruser.models import TweeterUser 


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username= data['username'],
                            password = data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', "/"))
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', "/"))

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TweeterUser.objects.create(
                username = data['username'],
                display_name = data['display_name'],
                password = data['password']
            )
            return HttpResponseRedirect("/login/")
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})