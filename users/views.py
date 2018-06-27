from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .templates.users.forms import UserCreateForm
from django.shortcuts import render, redirect
from .models import User


def index(request):
    totalUsers = User.objects.count()
    return render(request, 'users/index.html', { 'num_users': totalUsers })
    return HttpResponse("Hello, world. You're at the users index. We have {} users signed up so far!".format(totalUsers))

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreateForm()
    return render(request, 'users/signup.html', {'form': form})

def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("user does not exist")
    return render(request, 'users/detail.html', {'user': user})
