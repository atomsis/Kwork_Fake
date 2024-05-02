from django.shortcuts import render
from .models import CustomerProfile, PerformerProfile

def customer_profile(request):
    profile = CustomerProfile.objects.get(user=request.user)
    return render(request, 'profiles/customer_profile.html', {'profile': profile})

def performer_profile(request):
    profile = PerformerProfile.objects.get(user=request.user)
    return render(request, 'profiles/performer_profile.html', {'profile': profile})

