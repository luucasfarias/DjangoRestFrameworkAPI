from django.db import models

# Create your models here.

# CreateUser de teste: lucas | 122114karol

from django.conf import settings
from django.db import models
from django.template import defaultfilters
from django.utils.translation import ugettext_lazy as _


class Sprint(models.Model):
    """Período de interação do desenvolvimento"""

    name = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


class Task(models.Model):
    """Unidade refere-se a tarefa que será realizado em casa sprint"""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not started')),
        (STATUS_IN_PROGRESS, _('In progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
