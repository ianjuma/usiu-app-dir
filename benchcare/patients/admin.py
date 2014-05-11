from django.contrib import admin
from patients.models import Patient, Next_of_Kin, Vitals, Visits, Diagnosis, Medication, History


class Next_of_KinInLine(admin.StackedInline):
    model = Next_of_Kin
    extra = 1


class VitalsInLine(admin.StackedInline):
    model = Vitals
    extra = 1


class VisitsInLine(admin.StackedInline):
    model = Visits
    extra = 1


class DiagnosiInLine(admin.StackedInline):
    model = Diagnosis
    extra = 1


class MedicationInLine(admin.StackedInline):
    model = Medication
    extra = 1


class Patient_HistoryInlIne(admin.StackedInline):
    model = History
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['id_number']}),
        ('Patient Number', {'fields': ['patient_number']}),
        ('Surname', {'fields': ['surname']}),
        ('First Name', {'fields': ['first_name']}),
        ('Last Name', {'fields': ['last_name']}),

        ('Gender', {'fields': ['sex']}),
        ('Marriage Status', {'fields': ['marriage_status']}),

        ('Telephone Number', {'fields': ['telephone_number']}),
        ('Email Address', {'fields': ['email_address']}),
        ('Education', {'fields': ['education']}),
        ('Occupation', {'fields': ['occupation']})


    ]
    inlines = [VitalsInLine, Next_of_KinInLine, VisitsInLine, DiagnosiInLine]
    list_display = ('surname', 'first_name', 'last_name', 'sex', 'marriage_status', 'education', 'occupation', 'telephone_number', 'email_address')
    list_filter = ['sex']
    search_fields = ['id_number', 'first_name', 'last_name']


admin.site.register(Patient, PatientAdmin)
