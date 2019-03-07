from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from .utils import AGENT_GROUP, EXPORT_GROUP


class Agent(models.Model):
    CDMX = 'CDMX'
    QRO = 'QRO'
    MTY = 'MTY'
    ECUADOR = 'ECUADOR'
    CHINA = 'CHINA'

    OFFICE_OPTIONS = ((CDMX, 'Ciudad de México'),
                      (QRO, 'Querétaro'),
                      (MTY, 'Monterrey'),
                      (ECUADOR, 'Ecuador'),
                      (CHINA, 'China'))


    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    office = models.CharField(max_length=255,
                              choices=OFFICE_OPTIONS,
                              default=CDMX)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """ Override the save method to add the client group.
        """
        if self.office == self.CHINA:
            user_group = Group.objects.get_or_create(name=EXPORT_GROUP)[0]
        else:
            user_group = Group.objects.get_or_create(name=AGENT_GROUP)[0]
        self.user.groups.add(user_group)
        return super(Agent, self).save(*args, **kwargs)

    def __str__(self):
        """ Return the string representation of the user
        related to this agent.
        """
        return str(self.user.get_full_name())


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        user_group = Group.objects.get_or_create(name=ADMIN_GROUP)[0]
        self.user.groups.add(user_group)
        return super(Agent, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user.get_full_name())
