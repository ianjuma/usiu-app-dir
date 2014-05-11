import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from patients.models import Patient, Next_of_Kin, Vitals, Visits, Diagnosis, Medication, History, Documents
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from patients.forms import PatientForm, Next_of_KinForm, VitalsForm, VisitsForm, DiagnosisForm, MedicationForm, HistoryForm, DocumentsForm


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


### Patient Views
@login_required
def index(request):
    if not request.user:
        raise PermissionDenied()
    context = RequestContext(request)

    return render_to_response("basedashboard.html")


@login_required
def calendar(request):
    if not request.user:
        raise PermissionDenied()
    context = RequestContext(request)

    return render_to_response("patients/calendar.html")


class CreatePatientView(LoggedInMixin, CreateView):
    context_object_name = 'newpatient'
    model = Patient
    form = PatientForm
    template_name = 'patients/add_patient.html'

    def get_success_url(self):
        return reverse('patientslist')


class ListPatientView(LoggedInMixin, ListView):
    context_object_name = 'patientslist'
    model = Patient
    template_name = 'patients/patients_list.html'

    def get_queryset(self):
        return Patient.objects.all()[:20]


class UpdatePatientView(LoggedInMixin, UpdateView):
    context_object_name = 'patientsupdate'
    model = Patient
    template_name = 'patients/updatepatient.html'

    def get_success_url(self):
        return reverse('patientslist')


class DetailPatientView(LoggedInMixin, DetailView):
    context_object_name = 'patientdetails'
    model = Patient
    template_name = 'patients/patientdetails.html'

    def get_queryset(self):
        return Patient.objects.all()


class DeletePatientView(LoggedInMixin, DeleteView):
    context_object_name = 'patientsdelete'
    model = Patient
    template_name = 'patients/delete_patient.html'

    def get_success_url(self):
        return reverse('patientslist')


### Patient Next of Kin Views
class CreateNext_of_Kin_View(LoggedInMixin, CreateView):
    context_object_name = 'nextofkin'
    form = Next_of_KinForm
    model = Next_of_Kin
    template_name = 'patients/new_nextofkin.html'

    def get_success_url(self):
        return reverse('patientslist')


class UpdateNext_of_Kin(LoggedInMixin, UpdateView):
    context_object_name = 'updatenextofkin'
    model = Next_of_Kin
    template_name = 'patients/updatenextofkin.html'

    def get_success_url(self):
        return reverse('patientslist')


class ListNext_of_Kin_View(LoggedInMixin, ListView):
    context_object_name = 'nextofkinlist'
    model = Next_of_Kin
    template_name = 'patients/nextofkin_list.html'

    def get_queryset(self):
        return Next_of_Kin.objects.all()


class DetailNext_of_Kin(LoggedInMixin, DetailView):
    context_object_name = 'nextofkindetail'
    model = Next_of_Kin
    template_name = 'patients/nextofkindetail.html'

    def get_queryset(self):
        return Next_of_Kin.objects.all()


class DeleteNext_of_KinView(LoggedInMixin, DeleteView):
    context_object_name = 'deletenextofkin'
    model = Next_of_Kin
    template_name = 'patients/delete_nextofkin.html'

    def get_success_url(self):
        return reverse('patientslist')


### Patients Vitals Views
class CreateVitalsView(LoggedInMixin, CreateView):
    context_object_name = 'vitals'
    model = Vitals
    form = VitalsForm
    template_name = 'patients/vitals.html'

    def get_success_url(self):
        return reverse('patientslist')


class ListVitalsView(LoggedInMixin, ListView):
    context_object_name = 'listvitals'
    model = Vitals
    template_name = 'patients/listvitals.html'

    def get_queryset(self):
        return Vitals.objects.all()


class UpdateVitalsView(LoggedInMixin, UpdateView):
    context_object_name = 'updatevitals'
    model = Vitals
    template_name = 'patients/updatevitals.html'

    def get_success_url(self):
        return reverse('patientslist')


class DetailVitalView(LoggedInMixin, DetailView):
    context_object_name = 'detailvitals'
    model = Vitals
    template_name = 'patients/detailvitals.html'

    def get_queryset(self):
        return Vitals.objects.all()


class DeleteVitalsView(LoggedInMixin, DeleteView):
    context_object_name = 'vitalsdelete'
    model = Vitals
    template_name = 'patients/delete_vitals.html'

    def get_success_url(self):
        return reverse('patientslist')


### Patient Visits View
class CreateVisitsView(LoggedInMixin, CreateView):
    context_object_name = 'visits'
    form = VisitsForm
    model = Visits
    template_name = 'patients/visits.html'

    def get_success_url(self):
        return reverse('patientslist')


class ListVisitsView(LoggedInMixin, ListView):
    context_object_name = 'visitslist'
    model = Visits
    template_name = 'patients/visitslist.html'

    def get_queryset(self):
        return Visits.objects.all()


class UpdateVisitsView(LoggedInMixin, UpdateView):
    context_object_name = 'updatevisits'
    model = Visits
    template_name = 'patients/updatevisits.html'

    def get_success_url(self):
        return reverse('patientslist')


class DetailVisitsView(LoggedInMixin, DetailView):
    context_object_name = 'detailvisits'
    model = Visits
    template_name = 'patients/detailvisits.html'


class DeleteVisitsView(LoggedInMixin, DeleteView):
    context_object_name = 'visitsdelete'
    model = Visits
    template_name = 'patients/delete_visits.html'

    def get_success_url(self):
        return reverse('patientslist')


### Diagnosis
class CreateDiagnosisView(LoggedInMixin, CreateView):
    context_object_name = 'newdiagnosis'
    form = DiagnosisForm
    model = Diagnosis
    template_name = 'patients/add_diagnosis.html'

    def get_success_url(self):
        return reverse('diagnosislist')


class ListDiagnosisView(LoggedInMixin, ListView):
    context_object_name = 'diagnosislist'
    model = Diagnosis
    template_name = 'patients/diagnosis_list.html'

    def get_queryset(self):
        return Diagnosis.objects.all()[:20]


class UpdateDiagnosisView(LoggedInMixin, UpdateView):
    context_object_name = 'diagnosisupdate'
    model = Diagnosis
    template_name = 'patients/updatediagnosis.html'

    def get_success_url(self):
        return reverse('diagnosislist')


class DetailDiagnosisView(LoggedInMixin, DetailView):
    context_object_name = 'diagnosisdetails'
    model = Diagnosis
    template_name = 'patients/diagnosisdetails.html'

    def get_queryset(self):
        return Diagnosis.objects.all()


class DeleteDiagnosisView(LoggedInMixin, DeleteView):
    context_object_name = 'diagnosisdelete'
    model = Diagnosis
    template_name = 'patients/delete_diagnosis.html'

    def get_success_url(self):
        return reverse('diagnosislist')


### Medication
class CreateMedicationView(LoggedInMixin, CreateView):
    context_object_name = 'newmedication'
    form = MedicationForm
    model = Medication
    template_name = 'patients/add_medication.html'

    def get_success_url(self):
        return reverse('medicationlist')


class ListMedicationView(LoggedInMixin, ListView):
    context_object_name = 'medicationlist'
    model = Medication
    template_name = 'patients/medication_list.html'

    def get_queryset(self):
        return Medication.objects.all()[:20]


class UpdateMedicationView(LoggedInMixin, UpdateView):
    context_object_name = 'medicationsupdate'
    model = Medication
    template_name = 'patients/medicationsupdate.html'

    def get_success_url(self):
        return reverse('medicationlist')


class DetailMedicationView(LoggedInMixin, DetailView):
    context_object_name = 'medicationdetails'
    model = Medication
    template_name = 'patients/medicationsdetails.html'

    def get_queryset(self):
        return Medication.objects.all()


class DeleteMedicationView(LoggedInMixin, DeleteView):
    context_object_name = 'medicationsdelete'
    model = Medication
    template_name = 'patients/delete_medication.html'

    def get_success_url(self):
        return reverse('medicationlist')


### History
class CreateHistoryView(LoggedInMixin, CreateView):
    context_object_name = 'newhistory'
    form = HistoryForm
    model = History
    template_name = 'patients/add_history.html'

    def get_success_url(self):
        return reverse('historylist')


class ListHistoryView(LoggedInMixin, ListView):
    context_object_name = 'historylist'
    model = History
    template_name = 'patients/history_list.html'

    def get_queryset(self):
        return History.objects.all()[:20]


class UpdateHistoryView(LoggedInMixin, UpdateView):
    context_object_name = 'historyupdate'
    model = History
    template_name = 'patients/historyupdate.html'

    def get_success_url(self):
        return reverse('historylist')


class DetailHistoryView(LoggedInMixin, DetailView):
    context_object_name = 'historydetails'
    model = History
    template_name = 'patients/historydetails.html'

    def get_queryset(self):
        return Medication.objects.all()


class DeleteHistoryView(LoggedInMixin, DeleteView):
    context_object_name = 'historydelete'
    model = History
    template_name = 'patients/delete_history.html'

    def get_success_url(self):
        return reverse('historylist')
