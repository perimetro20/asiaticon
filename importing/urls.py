from django.urls import path
from .views import clients, new_client, client, edit_client, activate_client, \
                   deactivate_client, new_import_request, import_request, import_requests, \
                   new_import_response, import_response, import_responses, \
                   containers, edit_container, format_31

app_name = 'importing'

urlpatterns = [
    path('clients/', clients, name='clients'),
    path('client/<int:client_id>/new_import_request/', new_import_request, name='new_import_request'),
    path('clients/new', new_client, name='new_client'),
    path('clients/<int:client_id>/', client, name='client'),
    path('clients/<int:client_id>/edit/', edit_client, name='edit_client'),
    path('clients/<int:client_id>/activate/', activate_client, name='activate_client'),
    path('clients/<int:client_id>/deactivate/', deactivate_client, name='deactivate_client'),
    path('import_request/<int:import_request_id>/', import_request, name='import_request'),
    path('import_requests/', import_requests, name='import_requests'),
    path('import_response/new/<int:import_request_id>/', new_import_response, name='new_import_response'),
    path('import_response/<int:import_response_id>/', import_response, name='import_response'),
    path('import_responses/', import_responses, name='import_responses'),
    path('containers/', containers, name='containers'),
    path('container/<int:container_id>/edit/', edit_container, name='edit_container'),
    path('format_31/<int:import_response_id>/', format_31, name='format_31')
]
