from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context= {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    errors=Course.objects.validation(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    if request.method == "POST":
        Course.objects.create (
            name = request.POST["name"],
            description = request.POST["description"]
        )
        return redirect('/')

def show(request, course_id):
    context = {
        "course":Course.objects.get(id=course_id)
    }
    return render(request, 'destroy.html', context)


def destroy(request, course_id):
    course_to_remove= Course.objects.get(id=course_id)
    course_to_remove.delete()
    return redirect('/')