import os
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, ImportRequestForm, ImportResponseForm, ContainerForm
from .models import Client, ImportRequest, ImportResponse, Container
from user_profiles.utils import is_export, is_agent

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
def import_request(request, import_request_id):
    import_request = get_object_or_404(ImportRequest, pk=import_request_id)
    context['import_request'] = import_request
    return render(request, 'importing/import_request.html', context)


@login_required
def import_requests(request):
    if is_export(request.user) and not is_agent(request.user):
        import_requests = ImportRequest.objects.filter(export_agent=request.user.agent)
    else:
        import_requests = ImportRequest.objects.all()
    context['import_requests'] = import_requests
    return render(request, 'importing/import_requests.html', context)


@login_required
def new_import_response(request, import_request_id):
    if request.method == 'GET':
        import_request = ImportRequest.objects.get(pk=import_request_id)
        form = ImportResponseForm(initial={'import_request': import_request})
        context['title'] = 'Answer Request'
        context['action'] = 'Answer Request'
        context['form'] = form
        return render(request, 'importing/form.html', context)
    elif request.method == 'POST':
        form = ImportResponseForm(request.POST)
        if form.is_valid():
            import_response = form.save()
            return redirect('importing:import_response', import_response.id)
        else:
            context['title'] = 'Answer Request'
            context['action'] = 'Answer Request'
            context['form'] = form
            return render(request, 'importing/form.html', context)


def import_response(request, import_response_id):
    import_response = get_object_or_404(ImportResponse, pk=import_response_id)
    context['import_response'] = import_response
    return render(request, 'importing/import_response.html', context)


def import_responses(request):
    import_responses = ImportResponse.objects.all()
    context['import_responses'] = import_responses
    return render(request, 'importing/import_responses.html', context)


@login_required
def new_import_request(request, client_id):
    if request.method == 'GET':
        client = Client.objects.get(pk=client_id)
        form = ImportRequestForm(initial={'client': client})
        context['title'] = 'Create Import Request'
        context['action'] = 'Create Import Request'
        context['form'] = form
        return render(request, 'importing/image_form.html', context)
    elif request.method == 'POST':
        form = ImportRequestForm(request.POST, request.FILES)
        if form.is_valid():
            import_request = form.save()
            return redirect('importing:import_request', import_request.id)
        else:
            print(form.errors)
            context['title'] = 'Create New Import Request'
            context['action'] = 'Create Import Request'
            context['form'] = form

            return render(request, 'importing/image_form.html', context)


@login_required
def containers(request):
    containers = Container.objects.all()
    context['containers'] = containers
    return render(request, 'importing/containers.html', context)


@login_required
def edit_container(request, container_id):
    container = get_object_or_404(Container,
                            pk=container_id)
    if request.method == 'GET':
        form = ContainerForm(instance=container)
        context['title'] = 'Edit Container'
        context['action'] = 'Save'
        context['form'] = form
        return render(request, 'importing/form.html', context)
    elif request.method == 'POST':
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            container = form.save()
            return redirect('importing:containers')
        else:
            context['title'] = 'Edit Container'
            context['action'] = 'Save'
            context['form'] = form
        return render(request, 'importing/form.html', context)
    return render(request, )


@login_required
def clients(request):
    active_clients = Client.objects.filter(status=Client.ACTIVE)
    inactive_clients = Client.objects.filter(status=Client.INACTIVE)
    clients = Client.objects.all()
    context['active_clients'] = active_clients
    context['inactive_clients'] = inactive_clients

    return render(request, 'importing/clients.html', context)


@login_required
def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    context['client'] = client
    return render(request, 'importing/client.html', context)


@login_required
def new_client(request):
    if request.method == 'GET':
        form = ClientForm
        context['title'] = 'Create New Client'
        context['action'] = 'Create Client'
        context['form'] = form
        return render(request, 'importing/form.html', context)
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('importing:client', client.id)
        else:
            context['title'] = 'Create New Client'
            context['action'] = 'Create Client'
            context['form'] = form

            return render(request, 'importing/form.html', context)


@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client,
                            pk=client_id)
    if request.method == 'GET':
        form = ClientForm(instance=client)
        context['title'] = 'Edit Client'
        context['action'] = 'Save'
        context['form'] = form
        return render(request, 'importing/form.html', context)
    elif request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('importing:client', client_id=client.id)
        else:
            context['title'] = 'Edit Client'
            context['action'] = 'Save'
            context['form'] = form
        return render(request, 'importing/form.html', context)


@login_required
def activate_client(request, client_id):
    client = get_object_or_404(Client,
                               pk=client_id)
    if request.method == 'POST':
        client.status = Client.ACTIVE
        client.save()
        return redirect('importing:clients')


@login_required
def deactivate_client(request, client_id):
    client = get_object_or_404(Client,
                               pk=client_id)
    if request.method == 'POST':
        client.status = Client.INACTIVE
        client.save()
        return redirect('importing:clients')


def format_31(request, import_response_id):
    format = get_object_or_404(ImportResponse, pk=import_response_id)
    # form = FormatForm(instance=format)
    context['format'] = format
    return render(request, 'importing/format_31.html', context)

