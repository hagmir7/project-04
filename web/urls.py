from django.urls import path
from .views import *


urlpatterns = [
	path('', home, name='home'),
	path('users', users, name='users'),
	path('events', events, name='events'),
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
	path('delete/group/<int:id>', delete_group, name='delete_group')

]   