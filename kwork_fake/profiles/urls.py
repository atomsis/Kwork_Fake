from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('customer/', views.customer_profile, name='customer_profile'),
    path('performer/', views.performer_profile, name='performer_profile'),
]
