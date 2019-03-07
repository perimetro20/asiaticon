import os
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm, AgentForm
from .models import Agent


access_key = os.environ['FORGE_KEY']
access_url = '&api_key={}'.format(access_key)
url = 'https://forex.1forge.com/1.0.3/quotes?pairs=USDMXN,USDCNH&api_key=I82Hd3XYYFGsUVAWvQFWv8fDsdcvAHrZ'
r = requests.get(url)
result = r.json()
context = {
    'usdmex': result[0]['price'],
    'usdcnh': result[1]['price']
}


@login_required
def agents(request):
    agents = Agent.objects.all()
    print(agents)
    context['agents'] = agents

    return render(request, 'user_profiles/agents.html', context)


@login_required
def new_agent(request):
    if request.method == 'GET':
        user_form = UserForm
        agent_form = AgentForm
        context['title'] = 'Create New Agent'
        context['action'] = 'Create Agent'
        context['forms'] = [user_form, agent_form]
        return render(request, 'importing/multiform.html', context)
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        agent_form = AgentForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if agent_form.is_valid():
                agent = agent_form.save(commit=False)
                user.save()
                agent.user = user
                agent.save()
                return redirect('user_profiles:agents')
            else:
                user.delete()
                context['title'] = 'Create New Agent'
                context['action'] = 'Create Agent'
                context['forms'] = [user_form, agent_form]
                return render(request, 'importing/multiform.html', context)
        else:
            context['title'] = 'Create New Agent'
            context['action'] = 'Create Agent'
            context['forms'] = [user_form, agent_form]
            return render(request, 'importing/multiform.html', context)
