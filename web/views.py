from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    context = {
        'name':'dashboard',
        'title': "Dashboard"
    }
    return render(request, 'index.html', context)
    

def users(request):
    context = {
        'name':'users',
        'title': "Members"
    }
    return render(request, 'users.html', context)

def events(request):
    context = {
        'name':'events',
        'title': "Événements"
    }
    return render(request, 'events.html', context)


def donors(request):
    context = {
        'name':'donors',
        'title': "Dons et donateur"
    }
    return render(request, 'donors.html', context)



def expenses(request):
    context = {
        'name':'expenses',
        'title': "Dépenses"
    }
    return render(request, 'expenses.html', context)

def emailing(request):
    context = {
        'name':'emailing',
        'title': "Emailing"
    }
    return render(request, 'emailing.html', context)

def calendar(request):
    context = {
        'name':'calendar',
        'title': "Calendrier"
    }
    return render(request, 'calendar.html', context)


def blogs(request):
    context = {
        'name':'blogs',
        'title': "Blogs"
    }
    return render(request, 'blogs.html', context)