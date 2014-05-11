from django.db import models
from patients.models import Patient
from patients.models import Vitals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import admin

# Create your models here.


class PatientAnalytic(Patient):
    def __unicode__(self):
        return '%s %s %s ' % (self.surname, self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Analytic')
        verbose_name_plural = _('Analytics')


class VitalsAnalytics(Vitals):
    def __unicode__(self):
        return '%s %s %s ' % (self.surname, self.first_name, self.last_name)

    class Meta:
        verbose_name = _('VitalAnalytic')
        verbose_name_plural = _('VitalAnalytics')
