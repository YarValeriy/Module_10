from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')
        # return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
            # return redirect('/')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')
        # return redirect('/')  # Redirect to home page after successful login
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:root')
        # return redirect('/')  # Redirect to home page after successful login

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required(login_url='quotes:root')
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')
    # return redirect('/')  # Redirect to home page after logout
