from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm
from profiles.models import CustomerProfile, PerformerProfile


def register(request):
    if request.user.is_authenticated:
        return redirect('account:logout')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            name = form.cleaned_data.get('name')
            contact_info = form.cleaned_data.get('contact_info')
            experience = form.cleaned_data.get('experience')

            user = form.save()

            CustomerProfile.objects.create(
                user=user,
                name=name,
                contact_info=contact_info,
                experience=experience
            )
            PerformerProfile.objects.create(
                user=user,
                name=name,
                contact_info=contact_info,
                experience=experience
            )
            return redirect('account:register_completed', username=username)
            # return render(request, 'accounts/register_complited.html', {'username': username})
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def register_completed(request, username):
    return render(request, 'accounts/register_complited.html', {'username': username})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile:customer_profile')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('profile:customer_profile')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('account:login')
