from django import forms
from .models import   Event


class event_form(forms.ModelForm):
    class Meta:
        model= Event
        fields={'name', 'event_start_date','event_end_date',}
