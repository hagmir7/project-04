from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
	path('dashboard', home, name='home'),
	path('users', login_required(users), name='users'),
	path('events', events, name='events'),
	path('event/<int:id>', events_detail, name='events_detail'),
	path('donors', donors, name='donors'),
	path('expenses', expenses, name='expenses'),
	path('emailing', emailing, name='emailing'),
	path('calendar', calendar, name='calendar'),
	path('blogs', blogs, name="blogs"),
	
	path('association', association, name='association'),
	path('create/association', create_association, name='create_association'),
	path('delete/association/<int:id>', delete_association, name="delete_association"),
	path('update/association/<int:id>', update_association, name='update_association'),

	path('create/member', create_member, name="create_mumber"),
	path('update/member/<int:id>', update_member, name='update_member'),
	path('delete/member/<int:id>', delete_member, name='delete_member'),

	path('create/event', create_event, name='create_event'),
	path('update/event/<int:id>', update_event, name='update_event'),
	path('delete/event/<int:id>', delete_event, name='delete_event'),

	path('create/donor', create_donor, name='create_donor'),
	path('update/donor/<int:id>', update_donor, name='update_donor'),
	path('delete/donor/<int:id>', delete_donor, name='delete_donor'),

	path('donors-ass', donors_ass, name='donors_ass'),
	path('create/donors_ass', create_donor_ass, name='create_donor_ass'),
	path('update/donors_ass/<int:id>', update_donor_ass, name='update_donor_ass'),
	path('delete/donors_ass/<int:id>', delete_donor_ass, name='delete_donor_ass'),

	path('create/expenses', create_expenses, name='create_expenses'),
	path('update/expenses/<int:id>', update_expenses, name='update_expenses'),
	path('delete/expenses/<int:id>', delete_expenses, name='delete_expenses'),

	path('cours', cours, name='cours'),
	path('cours/<int:id>', cours_detail, name='cours_detail'),
	path('create/cours', create_cours, name='create_cours'),
	path('update/cours/<int:id>', update_cours, name='update_cours'),
	path('delete/cours/<int:id>', delete_cours, name='delete_cours'),


	# Group
	path('group', group, name='group'),
	path('group/<int:id>', group_detail, name='group_detail'),
	path('create/group', create_group, name='create_group'),
	path('update/group/<int:id>', update_group, name='update_group'),
	path('delete/group/<int:id>', delete_group, name='delete_group'),
	# Tache
	path('tache', tache, name='tache'),
	path('tache/<int:id>', tache_detail, name='tache_detail'),
	path('create/tache', create_tache, name='create_tache'),
	path('update/tache/<int:id>', update_tache, name='update_tache'),
	path('delete/tache/<int:id>', delete_tache, name='delete_tache'),

	# Session
	path('session', session, name='session'),
	path('session/<int:id>', session_detail, name='session_detail'),
	path('create/session', create_session, name='create_session'),
	path('update/session/<int:id>', update_session, name='update_session'),
	path('delete/session/<int:id>', delete_session, name='delete_session'),


	# Evenement Participant
	path('evpa', evpa, name='evpa'),
	path('evpa/<int:id>', evpa_detail, name='evpa_detail'),
	path('create/evpa', create_evpa, name='create_evpa'),
	path('update/evpa/<int:id>', update_evpa, name='update_evpa'),
	path('delete/evpa/<int:id>', delete_evpa, name='delete_evpa'),


	# Participant
	path('participant', participant, name='participant'),
	path('participant/<int:id>', participant_detail, name='participant_detail'),
	path('create/participant', create_participant, name='create_participant'),
	path('update/participant/<int:id>', update_participant, name='update_participant'),
	path('delete/participant/<int:id>', delete_participant, name='delete_participant')
]   