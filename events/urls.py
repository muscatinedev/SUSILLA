

from django.urls import path, include

from events.views import events_home_view, add_event

app_name='events'



urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/',  events_home_view, name='events-home'),
    path('',  events_home_view, name='events-home'),
    path('add/',  add_event, name='add-event'),



]
