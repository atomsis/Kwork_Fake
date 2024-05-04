from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register-completed/<str:username>/', views.register_completed, name='register_completed'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
