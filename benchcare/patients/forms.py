from patients.models import Patient, Next_of_Kin, Vitals, Visits, Diagnosis, Medication, History, Documents
from django import forms


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient


class Next_of_KinForm(forms.ModelForm):
    class Meta:
        model = Next_of_Kin


class VitalsForm(forms.ModelForm):
    class Meta:
        model = Vitals


class VisitsForm(forms.ModelForm):
    class Meta:
        model = Visits


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
