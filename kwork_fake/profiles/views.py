from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomerProfile, PerformerProfile
from .forms import CustomerProfileForm, PerformerProfileForm


@login_required
def customer_profile(request):
    profile = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerProfileForm(instance=profile,
                                   data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profiles/customer_profile.html', {'form': form})
    else:
        form = CustomerProfileForm(instance=profile)
    return render(request, 'profiles/customer_profile.html', {'form': form,'section':'customer'})


@login_required
def performer_profile(request):
    profile = PerformerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PerformerProfileForm(instance=profile,
                                    data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile:performer_profile')
    else:
        form = PerformerProfileForm(instance=profile)
    return render(request, 'profiles/performer_profile.html', {'form': form,'section':'performer'})
