
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.views import View

def index(request):
    if request.user.is_authenticated.value:
        return redirect('projectman:dashboard')
    else:
        return render(request, 'projectman/index.html')


class login(View):

    def get(self, request):
        if request.user.is_authenticated and request.user.is_active:
            return redirect('projectman:dashboard')
        else:
            return  render(request, 'projectman/login.html')

    def post(self, request):
        if request.POST.get('username') is None:
            messages.error(request, "Error en usuario y/o contraseña")
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('projectman:dashboard')
            else:
                return redirect('projectman:login')


@login_required
def dashboard(request):
    return render(request, "projectman/dashboard.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect('projectman:index')


