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
	path('delete/expenses/<int:id>', delete_expenses, name='delete_expenses')

]   