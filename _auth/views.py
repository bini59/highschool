from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

# Create your views here.

def login_GET(request):
    if request.user.is_authenticated:
        return redirect('/')
    return auth_views.LoginView.as_view(template_name='_auth/login.html')(request)

