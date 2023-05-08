from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from inventory.models import Query, Stock
from inventory.forms import QueryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/login')
def query_create(request):
   
    if request.method == 'POST':
        user = request.user
        form = QueryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            query = form.save()
            return redirect('landing')
        
    else:
       form = QueryForm()

    return render(request,
            'query_form.html',
            {'form': form})