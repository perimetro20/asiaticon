from django.urls import path
from .views import new_agent, agents

app_name = 'user_profiles'

urlpatterns = [
    path('agents/', agents, name='agents'),
    path('agent/new', new_agent, name='new_agent')
]
