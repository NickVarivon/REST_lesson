from django.shortcuts import render, redirect

from .models import Persons


def index(request):
    persons = Persons.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'index.html', context)


def creat(request):
    if request.method == 'POST':
        person = Persons()
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.age = request.POST.get('age')
        person.save()
    return redirect("/")


def edit(request, id):
    person = Persons.objects.get(id=id)
    context = {
        'person': person
    }

    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.age = request.POST.get('age')
        person.save()
        return redirect("/")
    else:
        return render(request, 'edit.html', context)


def delete(request, id):
    person = Persons.objects.get(id=id)
    person.delete()
    return redirect("/")
