
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import *
from django.contrib import messages


def home(request):
    context = {
        'name': 'dashboard',
        'title': "Dashboard"
    }
    return render(request, 'index.html', context)

@login_required
def association(request):
    association = Association.objects.all()
    context = {
        'name': 'association',
        'title': "Association",
        'associations': association
    }
    return render(request, 'association.html', context)

@login_required
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

@login_required
def update_association(request, id):
    association = Association.objects.get(id=id)
    form = CrateAssociationForm(request.POST or None, instance=association)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Association modifiée avec succès...')
            return redirect('association')
    return render(request, 'update-association.html', {'form': form, 'association': association})

@login_required
def delete_association(request, id):
    association = Association.objects.get(id=id)
    association.delete()
    messages.success(request, 'Association supprimée avec succès...')
    return redirect('association')

@login_required
def users(request):
    association = Association.objects.all()
    member = Membre.objects.all().order_by('-id')
    context = {
        'association': association,
        'members': member,
        'name': 'users',
        'title': "Members"
    }
    return render(request, 'users.html', context)

@login_required
def create_member(request):
    if request.method == 'POST':
        form = CrateMemberForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member créée avec succès...')
            return redirect('users')
    else:
        return redirect('users')

@login_required
def delete_member(request, id):
    member = Membre.objects.get(id=id)
    member.delete()
    messages.success(request, 'Member supprimée avec succès...')
    return redirect('users')

@login_required
def update_member(request, id):
    association = Association.objects.all()
    member = Membre.objects.get(id=id)
    form = CrateMemberForm(instance=member)
    if request.method == 'POST':
        form = CrateMemberForm(
            request.POST, files=request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member modifiée avec succès...')
            return redirect('users')
        else:
            print('not valide')
            return redirect('users')
    context = {'form': form, 'member': member, 'association': association}
    return render(request, 'update-member.html', context)

@login_required
def events(request):
    events = Evenement.objects.all().order_by('-id')

    context = {
        'events': events,
        'name': 'events',
        'title': "Événements"
    }
    return render(request, 'events.html', context)

@login_required
def events_detail(request, id):
    event = Evenement.objects.get(id=id)
    context = {
        'event': event,
        'title': event.titre
    }
    return render(request, 'events-detail.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = CrateEventrForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Événement créée avec succès...')
            return redirect('events')
    else:
        return redirect('events')

@login_required
def update_event(request, id):
    event = Evenement.objects.get(id=id)
    form = CrateEventrForm(request.POST, files=request.FILES, instance=event)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Événement modifiée avec succès...')
            return redirect('events')
    context = {'event': event}
    return render(request, 'update-event.html', context)

@login_required
def delete_event(request, id):
    event = Evenement.objects.get(id=id)
    event.delete()
    messages.success(request, 'Événement supprimée avec succès...')
    return redirect('events')

@login_required
def donors(request):
    donors = Douateur.objects.all().order_by('-id')
    context = {
        'donors': donors,
        'name': 'donors',
        'title': "Dons et donateur"
    }
    return render(request, 'donors.html', context)

@login_required
def create_donor(request):
    if request.method == 'POST':
        form = CrateDonorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur créée avec succès...')
            return redirect('donors')
    else:
        return redirect('donors')

@login_required
def update_donor(request, id):
    donor = Douateur.objects.get(id=id)
    form = CrateDonorsForm(request.POST, instance=donor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Donateur modifiée avec succès...')
            return redirect('donors')
    context = {'donor': donor}
    return render(request, 'update-donor.html', context)

@login_required
def delete_donor(request, id):
    donor = Douateur.objects.get(id=id)
    donor.delete()
    messages.success(request, 'Donateur supprimée avec succès...')
    return redirect('donors')

@login_required
def donors_ass(request):
    donors_ass = DouateurAss.objects.all().order_by('-id')
    association = Association.objects.all().order_by('-id')
    douateur = Douateur.objects.all().order_by('-id')
    context = {
        'donors_ass': donors_ass,
        'douateur': douateur,
        'association': association,
        'name': 'donors-ass',
        'title': "Association et Donateur"
    }
    return render(request, 'donors_ass.html', context)

@login_required
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

@login_required
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
    context = {'association': association,
               'douateur': douateur, 'donor_ass': donor_ass}
    return render(request, 'update-donor-ass.html', context)

@login_required
def delete_donor_ass(request, id):
    donor = DouateurAss.objects.get(id=id)
    donor.delete()
    messages.success(request, 'Donateur supprimée avec succès...')
    return redirect('create_donor_ass')


#
# @login_required
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

@login_required
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
    context = {'expenses': expenses}
    return render(request, 'update-expenses.html', context)

@login_required
def delete_expenses(request, id):
    expenses = Depense.objects.get(id=id)
    expenses.delete()
    messages.success(request, 'Depense supprimée avec succès...')
    return redirect('expenses')

@login_required
def expenses(request):
    expenses = Depense.objects.all().order_by('-id')
    context = {
        'expenses': expenses,
        'name': 'expenses',
        'title': "Dépenses"
    }
    return render(request, 'expenses.html', context)

@login_required
def emailing(request):
    context = {
        'name': 'emailing',
        'title': "Emailing"
    }
    return render(request, 'emailing.html', context)

@login_required
def calendar(request):
    context = {
        'name': 'calendar',
        'title': "Calendrier"
    }
    return render(request, 'calendar.html', context)

@login_required
def blogs(request):

    context = {
        'name': 'blogs',
        'title': "Blogs"
    }
    return render(request, 'blogs.html', context)


# Cours
# @login_required
def cours(request):
    cours = Cours.objects.all().order_by('-id')
    association = Association.objects.all().order_by('-id')
    context = {
        'name': 'cours',
        'cours': cours,
        'title': "Courses",
        'association': association
    }
    return render(request, 'cours.html', context)

@login_required
def cours_detail(request, id):
    context = {}
    return render(request, 'cours-detail.html', context)

@login_required
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

@login_required
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
    context = {'cours': cours, 'association': association}
    return render(request, 'update-cours.html', context)

@login_required
def delete_cours(request, id):
    cours = Cours.objects.get(id=id)
    cours.delete()
    messages.success(request, 'Cours supprimée avec succès...')
    return redirect('cours')


@login_required# Group
def group(request):
    group = Group.objects.all().order_by('-id')
    cours = Cours.objects.all().order_by('-id')
    context = {
        'name': 'group',
        'group': group,
        'title': "groupes",
        'cours': cours
    }
    return render(request, 'group.html', context)

@login_required
def group_detail(request, id):
    context = {}
    return render(request, 'group-detail.html', context)

@login_required
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

@login_required
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
    context = {'group': group, 'cours': cours}
    return render(request, 'update-group.html', context)

@login_required
def delete_group(request, id):
    group = Group.objects.get(id=id)
    group.delete()
    messages.success(request, 'group supprimée avec succès...')
    return redirect('group')


@login_required# Tache
def tache(request):
    tache = Tache.objects.all().order_by('-id')
    association = Association.objects.all().order_by('-id')
    member = Membre.objects.all().order_by('-id')
    context = {
        'name': 'tache',
        'tache': tache,
        'title': "Tache",
        'associations': association,
        'members': member
    }
    return render(request, 'tache.html', context)

@login_required
def tache_detail(request, id):
    context = {}
    return render(request, 'tache-detail.html', context)

@login_required
def create_tache(request):
    form = CrateTacheForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'tache créée avec succès...')
            return redirect('tache')
        else:
            print('not valid')
            return redirect('tache')
    else:
        return redirect('tache')

@login_required
def update_tache(request, id):
    tache = Tache.objects.get(id=id)
    form = CrateTacheForm(request.POST, instance=tache)
    association = Association.objects.all().order_by('-id')
    member = Membre.objects.all().order_by('-id')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'tache créée avec succès...')
            return redirect('tache')
        else:
            return redirect('home')
    context = {
        'tache': tache,
        'associations': association,
        'members': member
    }
    return render(request, 'update-tache.html', context)

@login_required
def delete_tache(request, id):
    tache = Tache.objects.get(id=id)
    tache.delete()
    messages.success(request, 'tache supprimée avec succès...')
    return redirect('tache')



@login_required# session
def session(request):
    session = Session.objects.all().order_by('-id')
    events = Evenement.objects.all().order_by('-id')
    context = {
        'name': 'session',
        'session': session,
        'title': "session",
        'associations': association,
        'events': events
    }
    return render(request, 'session.html', context)

@login_required
def session_detail(request, id):
    context = {}
    return render(request, 'session-detail.html', context)

@login_required
def create_session(request):
    form = CrateSessionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'session créée avec succès...')
            return redirect('session')
        else:
            print('not valid')
            return redirect('session')
    else:
        return redirect('session')

@login_required
def update_session(request, id):
    session = Session.objects.get(id=id)
    form = CrateSessionForm(request.POST, instance=session)
    events = Evenement.objects.all().order_by('-id')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'session créée avec succès...')
            return redirect('session')
        else:
            return redirect('home')
    context = {
        'session': session,
        'associations': association,
        'events': events
    }
    return render(request, 'update-session.html', context)

@login_required
def delete_session(request, id):
    session = Session.objects.get(id=id)
    session.delete()
    messages.success(request, 'session supprimée avec succès...')
    return redirect('session')





@login_required# evpa
def evpa(request):
    evpa = EvenementParticipant.objects.all().order_by('-id')
    events = Evenement.objects.all().order_by('-id')
    participant = Participant.objects.all().order_by('-id')
    context = {
        'name': 'evpa',
        'evpa': evpa,
        'title': "evpa",
        'participant': participant,
        'events': events
    }
    return render(request, 'evpa.html', context)

@login_required
def evpa_detail(request, id):
    context = {}
    return render(request, 'evpa-detail.html', context)

@login_required
def create_evpa(request):
    form = CrateEvPaForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'evpa créée avec succès...')
            return redirect('evpa')
        else:
            print('not valid')
            return redirect('evpa')
    else:
        return redirect('evpa')

@login_required
def update_evpa(request, id):
    evpa = EvenementParticipant.objects.get(id=id)
    form = CrateEvPaForm(request.POST, instance=evpa)
    events = Evenement.objects.all().order_by('-id')
    participant = Participant.objects.all().order_by('-id')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'evpa créée avec succès...')
            return redirect('evpa')
        else:
            return redirect('home')
    context = {
        'evpa': evpa,
        'participant': participant,
        'events': events
    }
    return render(request, 'update-evpa.html', context)

@login_required
def delete_evpa(request, id):
    evpa = EvenementParticipant.objects.get(id=id)
    evpa.delete()
    messages.success(request, 'evpa supprimée avec succès...')
    return redirect('evpa')




    
@login_required# participant
def participant(request):
    participant = Participant.objects.all().order_by('-id')
    context = {
        'name': 'participant',
        'participant': participant,
        'title': "participant",
        'participant': participant,
        'events': events
    }
    return render(request, 'participant.html', context)

@login_required
def participant_detail(request, id):
    context = {}
    return render(request, 'participant-detail.html', context)

@login_required
def create_participant(request):
    form = CrateParticipantForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'participant créée avec succès...')
            return redirect('participant')
        else:
            print('not valid')
            return redirect('participant')
    else:
        return redirect('participant')

@login_required
def update_participant(request, id):
    participant = Participant.objects.get(id=id)
    form = CrateParticipantForm(request.POST or None, instance=participant )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'participant créée avec succès...')
            return redirect('participant')
        else:
            return redirect('home')
    context = {
        'participant': participant,
        'participant': participant,
        'events': events
    }
    return render(request, 'update-participant.html', context)

@login_required
def delete_participant(request, id):
    participant = Participant.objects.get(id=id)
    participant.delete()
    messages.success(request, 'participant supprimée avec succès...')
    return redirect('participant')