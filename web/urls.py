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
	path('blogs', blogs, name="blogs")

]   