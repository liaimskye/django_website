from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def user_login(request): 
    return render(request,'authentication:login.html')

def user_authenticate(request): 
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password= password)
        if user is None:
            return HttpResponseRedirect(
                reverse('authentication:login')
            )
        
        else:
            login(request,user)
            return HttpResponseRedirect(
                reverse('authentication:login')
            )
    else:
        return render(request, 'user.html')
    
def register(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid:
            form.save()
        return redirect(reverse("login"))
    else:
        form = UserCreationForm()
    return render(response, 'register.html', {'form':form})

def log_out(request):
    logout
    return  render(request,'base:landing')


