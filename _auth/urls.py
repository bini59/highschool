from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = '_auth'

urlpatterns = [
    path('login/', views.login_GET, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
