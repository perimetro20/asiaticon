from django import forms
from django.contrib.auth import get_user_model
from .models import Agent


class UserForm(forms.ModelForm):
    """ ModelForm for Users.
    This is the general model form for creating users.
    """

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'username': ('Email'),
            'first_name': ('Name'),
            'last_name': ('Lastname')
        }


class AgentForm(forms.ModelForm):
    """ ModelForm for Agents
    This is the general model form for creating users.
    """

    class Meta:
        model = Agent
        fields = [
            'office'
        ]
