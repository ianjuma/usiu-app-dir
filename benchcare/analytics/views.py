from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse
from analytics.models VitalsAnalytics
from analytics.models PatientAnalytic


def patientVital():
    patient = PatientAnalytic.objects.get(pk=1)
    # PatientAnalytic.objects.all()
    male = PatientAnalytic.objects.filter(sex="M")

    sec = PatientAnalytic.objects.filter(education__exact="S")
    college = PatientAnalytic.objects.filter(education__exact="C")

    age_over = PatientAnalytic.objects.filter(date_of_birth__mte="1992-03-1")

