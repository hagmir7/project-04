from msilib.schema import File
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import *
from django.contrib import messages




def home(request):
    context = {
        'name':'dashboard',
        'title': "Dashboard"
    }
    return render(request, 'index.html', context)

def association(request):
    association = Association.objects.all()
    context = {
        'name':'association',
        'title': "Association",
        'associations' : association
    }
    return render(request, 'association.html', context)

def create_association(request):
    form = CrateAssociationForm()
    if request.method == 'POST':
        form = CrateAssociationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Association créée avec succès...')
            return redirect('association')
    else:
        return redirect('home')

def update_association(request, id):
    association = Association.objects.get(id=id)
    form = CrateAssociationForm(request.POST or None, instance = association)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Association modifiée avec succès...')
            return redirect('association')
    return render(request, 'update-association.html', {'form':form,'association':association})       

def delete_association(request, id):
    association = Association.objects.get(id=id)
    association.delete()
    messages.success(request, 'Association supprimée avec succès...')
    return redirect('association')

    

def users(request):
    association = Association.objects.all()
    member = Membre.objects.all().order_by('-id')
    context = {
        'association': association,
        'members':member,
        'name':'users',
        'title': "Members"
    }
    return render(request, 'users.html', context)

def create_member(request):
    if request.method == 'POST':
        form = CrateMemberForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member créée avec succès...')
            return redirect('users')
    else:
        return redirect('users')


def delete_member(request, id):
    member = Membre.objects.get(id=id)
    member.delete()
    messages.success(request, 'Member supprimée avec succès...')
    return redirect('users')



def update_member(request, id):
    association = Association.objects.all()
    member = Membre.objects.get(id=id)
    form = CrateMemberForm(instance=member)
    if request.method == 'POST':
        form = CrateMemberForm(request.POST, files=request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member modifiée avec succès...')
            return redirect('users')
        else:
            print('not valide')
            return redirect('users')
    context = {'form':form, 'member':member, 'association':association}
    return render(request, 'update-member.html', context)
    


def events(request):
    events = Evenement.objects.all().order_by('-id')

    context = {
        'events': events,
        'name':'events',
        'title': "Événements"
    }
    return render(request, 'events.html', context)


def create_event(request):
    if request.method == 'POST':
        form = CrateEventrForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Événement créée avec succès...')
            return redirect('events')
    else:
        return redirect('events')


def update_event(request, id):
    event = Evenement.objects.get(id=id)
    form = CrateEventrForm(request.POST, files=request.FILES, instance=event)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Événement modifiée avec succès...')
            return redirect('events')
    context = {'event':event}
    return render(request, 'update-event.html', context)

def delete_event(request, id):
    event = Evenement.objects.get(id=id)
    event.delete()
    messages.success(request, 'Événement supprimée avec succès...')
    return redirect('events')



def donors(request):
    donors = Douateur.objects.all().order_by('-id')
    context = {
        'donors':donors,
        'name':'donors',
        'title': "Dons et donateur"
    }
    return render(request, 'donors.html', context)


def create_donor(request):
    if request.method == 'POST':
        form = CrateDonorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur créée avec succès...')
            return redirect('donors')
    else:
        return redirect('donors')


def update_donor(request, id):
    donor = Douateur.objects.get(id=id)
    form = CrateDonorsForm(request.POST, instance=donor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur modifiée avec succès...')
            return redirect('donors')
    context = {'donor':donor}
    return render(request, 'update-donor.html', context)


def delete_donor(request, id):
    donor = Douateur.objects.get(id=id)
    donor.delete()
    messages.success(request, 'Donateur supprimée avec succès...')
    return redirect('donors')




def donors_ass(request):
    donors_ass = DouateurAss.objects.all().order_by('-id')
    association = Association.objects.all().order_by('-id')
    douateur = Douateur.objects.all().order_by('-id')
    context = {
        'donors_ass':donors_ass,
        'douateur':douateur,
        'association':association,
        'name':'donors-ass',
        'title': "Association et Donateur"
    }
    return render(request, 'donors_ass.html', context)




def create_donor_ass(request):
    form = CrateDouateurAssForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur créée avec succès...')
            return redirect('create_donor_ass')
        else:
            return redirect('home')
    else:
        return redirect('donors_ass')



def update_donor_ass(request, id):
    donor_ass = DouateurAss.objects.get(id=id)
    form = CrateDouateurAssForm(request.POST, instance=donor_ass)
    association = Association.objects.all().order_by('-id')
    douateur = Douateur.objects.all().order_by('-id')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur créée avec succès...')
            return redirect('create_donor_ass')
        else:
            return redirect('home')
    context = {'association':association, 'douateur':douateur,'donor_ass':donor_ass}
    return render(request, 'update-donor-ass.html', context)


def delete_donor_ass(request, id):
    donor = DouateurAss.objects.get(id=id)
    donor.delete()
    messages.success(request, 'Donateur supprimée avec succès...')
    return redirect('create_donor_ass')


# 

def create_expenses(request):
    form = CrateDepenseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Depense créée avec succès...')
            return redirect('expenses')
        else:
            return redirect('expenses')
    else:
        return redirect('expenses')

def update_expenses(request, id):
    expenses = Depense.objects.get(id=id)
    form = CrateDepenseForm(request.POST, instance=expenses)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Depense créée avec succès...')
            return redirect('expenses')
        else:
            return redirect('home')
    context = {'expenses':expenses}
    return render(request, 'update-expenses.html', context)


def delete_expenses(request, id):
    expenses = Depense.objects.get(id=id)
    expenses.delete()
    messages.success(request, 'Depense supprimée avec succès...')
    return redirect('expenses')



def expenses(request):
    expenses = Depense.objects.all().order_by('-id')
    context = {
        'expenses':expenses,
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





# Cours

def cours(request):
    cours = Cours.objects.all().order_by('-id')
    association = Association.objects.all().order_by('-id')
    context = {
        'name':'cours',
        'cours': cours,
        'title': "Courses",
        'association': association
    }
    return render(request, 'cours.html', context)

def cours_detail(request, id):
    context = {}
    return render(request, 'cours-detail.html', context)

def create_cours(request):
    form = CrateCoursForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cours créée avec succès...')
            return redirect('cours')
        else:
            print('not valid')
            return redirect('cours')
    else:
        return redirect('cours')

def update_cours(request, id):
    cours = Cours.objects.get(id=id)
    form = CrateCoursForm(request.POST, instance=cours)
    association = Association.objects.all().order_by('-id')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cours créée avec succès...')
            return redirect('cours')
        else:
            return redirect('home')
    context = {'cours':cours, 'association':association}
    return render(request, 'update-cours.html', context)


def delete_cours(request, id):
    cours = Cours.objects.get(id=id)
    cours.delete()
    messages.success(request, 'Cours supprimée avec succès...')
    return redirect('cours')





# Group
def group(request):
    group = Group.objects.all().order_by('-id')
    cours = Cours.objects.all().order_by('-id')
    context = {
        'name':'group',
        'group': group,
        'title': "groupes",
        'cours': cours
    }
    return render(request, 'group.html', context)

def group_detail(request, id):
    context = {}
    return render(request, 'group-detail.html', context)

def create_group(request):
    form = CrateGroupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'group créée avec succès...')
            return redirect('group')
        else:
            print('not valid')
            return redirect('group')
    else:
        return redirect('group')

def update_group(request, id):
    group = Group.objects.get(id=id)
    form = CrateGroupForm(request.POST, instance=group)
    cours = Cours.objects.all().order_by('-id')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'group créée avec succès...')
            return redirect('group')
        else:
            return redirect('home')
    context = {'group':group, 'cours':cours}
    return render(request, 'update-group.html', context)


def delete_group(request, id):
    group = Group.objects.get(id=id)
    group.delete()
    messages.success(request, 'group supprimée avec succès...')
    return redirect('group')