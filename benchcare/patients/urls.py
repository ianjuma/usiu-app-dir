from django.conf.urls import patterns, url
from patients import views
from patients.views import CreatePatientView, ListPatientView, UpdatePatientView, DetailPatientView, DeletePatientView
from patients.views import CreateNext_of_Kin_View, UpdateNext_of_Kin, ListNext_of_Kin_View, DetailNext_of_Kin, DeleteNext_of_KinView
from patients.views import CreateVitalsView, ListVitalsView, UpdateVitalsView, DetailVitalView, DeleteVitalsView
from patients.views import CreateVisitsView, ListVisitsView, UpdateVisitsView, DetailVisitsView, DeleteVisitsView
from patients.views import CreateDiagnosisView, ListDiagnosisView, UpdateDiagnosisView, DetailDiagnosisView, DeleteDiagnosisView
from patients.views import CreateMedicationView, ListMedicationView, UpdateMedicationView, DetailMedicationView, DeleteMedicationView
from patients.views import CreateHistoryView, ListHistoryView, UpdateHistoryView, DetailHistoryView, DeleteHistoryView


urlpatterns = patterns('',

                       ### Patient Urls

                       url(r'^$', views.index, name='patientsindex'),
                       url(r'^newpatients/', CreatePatientView.as_view(),
                           name='newpatients',),
                       url(r'^patientslist/', ListPatientView.as_view(),
                           name='patientslist',),
                       url(r'^patientsupdate/(?P<pk>\d+)$',
                           UpdatePatientView.as_view(
                           ), name='patientsupdate',),
                       url(r'^patientsdetails(?P<pk>\d+)$/',
                           DetailPatientView.as_view(
                           ), name='patientsdetails',),
                       url(r'^patientsdelete(?P<pk>\d+)$/',
                           DeletePatientView.as_view(
                           ), name='patientsdelete',),

                       ### Next of kin urls

                       url(r'^nextofkin/', CreateNext_of_Kin_View.as_view(),
                           name='nextofkin',),
                       url(r'^nextofkinlist/', ListNext_of_Kin_View.as_view(),
                           name='nextofkinlist',),
                       url(r'^updatenextofkin/(?P<pk>\d+)$',
                           UpdateNext_of_Kin.as_view(
                           ), name='updatenextofkin',),
                       url(r'^nextofkindetail(?P<pk>\d+)$/',
                           DetailNext_of_Kin.as_view(
                           ), name='nextofkindetail',),
                       url(r'^deletenextofkin(?P<pk>\d+)$/',
                           DeleteNext_of_KinView.as_view(
                           ), name='deletenextofkin',),

                       ### Vitals urls

                       url(r'^vitals/',
                           CreateVitalsView.as_view(), name='vitals',),
                       url(r'^listvitals/',
                           ListVitalsView.as_view(), name='listvitals',),
                       url(r'^updatevitals/(?P<pk>\d+)$',
                           UpdateVitalsView.as_view(), name='updatevitals',),
                       url(r'^detailvitals(?P<pk>\d+)$/', DetailVitalView.as_view(
                       ), name='detailvitals',),
                       url(r'^vitalsdelete(?P<pk>\d+)$/',
                           DeleteVitalsView.as_view(), name='vitalsdelete',),

                       ### Visits url

                       url(r'^visits/',
                           CreateVisitsView.as_view(), name='visits',),
                       url(r'^visitslist/',
                           ListVisitsView.as_view(), name='visitslist',),
                       url(r'^updatevisits/(?P<pk>\d+)$',
                           UpdateVisitsView.as_view(), name='updatevisits',),
                       url(r'^detailvisits(?P<pk>\d+)$/',
                           DetailVisitsView.as_view(), name='detailvisits',),
                       url(r'^visitsdelete(?P<pk>\d+)$/',
                           DeleteVisitsView.as_view(), name='visitsdelete',),

                       ### Diagnosis url

                       url(r'^newdiagnosis/', CreateDiagnosisView.as_view(),
                           name='newdiagnosis',),
                       url(r'^diagnosislist/', ListDiagnosisView.as_view(),
                           name='diagnosislist',),
                       url(r'^diagnosisupdate/(?P<pk>\d+)$',
                           UpdateDiagnosisView.as_view(
                           ), name='diagnosisupdate',),
                       url(r'^diagnosisdetail(?P<pk>\d+)$/',
                           DetailDiagnosisView.as_view(
                           ), name='diagnosisdetail',),
                       url(r'^diagnosisdelete(?P<pk>\d+)$/',
                           DeleteDiagnosisView.as_view(
                           ), name='diagnosisdelete',),

                       ### Medication urls

                       url(r'^newmedication/', CreateMedicationView.as_view(),
                           name='newmedication',),
                       url(r'^medicationlist/', ListMedicationView.as_view(),
                           name='medicationlist',),
                       url(r'^medicationsupdate/(?P<pk>\d+)$',
                           UpdateMedicationView.as_view(
                           ), name='medicationsupdate',),
                       url(r'^medicationdetails(?P<pk>\d+)$/',
                           DetailMedicationView.as_view(
                           ), name='medicationdetails',),
        url(r'^medicationsdelete(?P<pk>\d+)$/',
            DeleteMedicationView.as_view(), name='medicationsdelete',),

        ### Medical History urls

        url(r'^newhistory/', CreateHistoryView.as_view(),
            name='newhistory',),
        url(r'^historylist/', ListHistoryView.as_view(),
            name='historylist',),
        url(r'^historyupdate/(?P<pk>\d+)$',
            UpdateHistoryView.as_view(), name='historyupdate',),
        url(r'^historydetails(?P<pk>\d+)$/',
            DetailHistoryView.as_view(), name='historydetails',),
        url(r'^historydelete(?P<pk>\d+)$/',
            DeleteHistoryView.as_view(), name='historydelete',),



        )
