from django import forms
from django.contrib.auth.models import User
from .models import Client, ImportRequest, ImportResponse, Container
from user_profiles.models import Agent
from user_profiles.utils import EXPORT_GROUP

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'email',
            'agent',
            'phone_number',
            'whatsapp',
            'wechat',
            'comments',
        ]


class ImportRequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImportRequestForm, self).__init__(*args, **kwargs)
        export_users = User.objects.filter(groups__name=EXPORT_GROUP)
        export_agents = Agent.objects.filter(user__in=export_users)
        self.fields['export_agent'].queryset = export_agents

    class Meta:
        model = ImportRequest
        fields = [
            'client',
            'photo',
            'product_name',
            'quantity',
            'comments',
            'aeroshipment',
            'export_agent'
        ]

        widgets = {
            'client': forms.HiddenInput(),
        }

class ImportResponseForm(forms.ModelForm):
    class Meta:
        model = ImportResponse
        fields = [
            'import_request',
            'hs_code',
            'material',
            'height',
            'width',
            'depth',
            'weight',
            'color',
            'time_production',
            'moq',
            'total_pieces',
            'pieces_carton',
            'box_height',
            'box_width',
            'box_depth',
            'total_cbm',
            'fob_price',
            'comments',
            'supplier_information'
        ]
        widgets = {
            'import_request': forms.HiddenInput(),
        }


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = '__all__'
        widgets = {
            'container': forms.HiddenInput(),
        }
