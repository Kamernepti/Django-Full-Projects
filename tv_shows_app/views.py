from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    context= {
        "shows": Show.objects.all()
    }
    return render(request, 'shows.html', context)

def profile(request, show_id):
    context= {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, 'profile.html', context)

def edit(request, show_id):
    context = {
        "show" :Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    context ={
        "show": Show.objects.get(id=show_id)
    }
    if request.method=="POST":
        newedit = Show.objects.get(id=show_id)
        newedit.title = request.POST["title"]
        newedit.network = request.POST["network"]
        newedit.release_date = request.POST["release_date"]
        newedit.desc = request.POST["desc"]
        newedit.save()
    return redirect('/shows')

def new(request):
    return render(request, 'new.html')

def add_show(request):
    if request.method == "POST":
        Show.objects.create(
            title= request.POST["title"],
            network= request.POST["network"],
            release_date=request.POST["release_date"],
            desc= request.POST["desc"]
        )
    return redirect('/shows')

def destroy(request, show_id):
    show_to_delete=Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')
