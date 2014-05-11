from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import admin


class Patient(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    MARRIAGE_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widowed'),
        ('D', 'Divorced'),
    )
    EDUCATION = (
        ('N', 'None'),
        ('P', 'Primary'),
        ('S', 'Seconday/High School'),
        ('C', 'College/University?Graduate'),
    )
    id_number = models.IntegerField(db_index=True)
    patient_number = models.IntegerField(db_index=True)
    surname = models.CharField(max_length=400)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    sex = models.CharField(max_length=2, choices=GENDER)
    date_of_birth = models.DateField(auto_now=True)
    marriage_status = models.CharField(max_length=4, choices=MARRIAGE_STATUS)
    occupation = models.CharField(max_length=500)
    education = models.CharField(max_length=4, choices=EDUCATION)
    telephone_number = models.IntegerField()
    post_address = models.CharField(max_length=400)
    email_address = models.EmailField(max_length=75)
    family_medical_history = models.TextField(max_length=1000)

    def __unicode__(self):
        return '%s %s %s ' % (self.surname, self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')


class Next_of_Kin(models.Model):
    patient_details = models.ForeignKey(Patient)
    kin_relation = models.CharField(max_length=200)
    kin_surname = models.CharField(max_length=400)
    kin_first_name = models.CharField(max_length=400)
    kin_last_name = models.CharField(max_length=400)
    kin_phone_number = models.IntegerField()
    kin_email_address = models.EmailField(max_length=75)

    def __unicode__(self):
        return '%s %s %s %s ' % (self.kin_relation, self.kin_surname, self.kin_first_name, self.kin_last_name)

    class Meta:
        verbose_name = _('Next of Kin')
        verbose_name_plural = _('Next of Kins')


class Vitals(models.Model):
    patient_vitals = models.ForeignKey(Patient)
    height = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    weight = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    temperature = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    pulse = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    respiratory_ration = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    blood_pressure = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")
    blood_oxygen = models.IntegerField(
        blank=True, null=True, help_text="Measured in  .")

    def __unicode__(self):
        return '%s %s %s %s %s %s %s ' % (self.patient_vitals, self.height, self.weight, self.temperature, self.pulse, self.respiratory_ration, self.blood_pressure)

    class Meta:
        verbose_name = _('PatientVital')
        verbose_name_plural = _('PatientVitals')


class Visits (models.Model):
    chief_complaint = models.TextField(max_length=1000, blank=True, null=True)
    patient_visits = models.ForeignKey(Patient, blank=True, null=True)

    def __unicode__(self):
        return self.chief_complaint

    class Meta:
        verbose_name = _('Complaint')
        verbose_name_plural = _('Complaints')


class Diagnosis(models.Model):
    TEST_CHOICES = (
        ('None', 'None'),
        ('Blood Test', 'Blood Test'),
        ('Malaria Test', 'Malaria Test'),
    )
    patient_diagnosis = models.TextField(
        max_length=5000, blank=True, null=True)
    patient_test = models.CharField(
        max_length=250, choices=TEST_CHOICES, blank=True, null=True)
    patient_test_results = models.TextField(
        max_length=5000, blank=True, null=True)
    patientdetails = models.ForeignKey(Patient, blank=True, null=True)

    def __unicode__(self):
        return self.patient_diagnosis

    class Meta:
        verbose_name = _('PatientDiagnosis')
        verbose_name_plural = _('PatientDiagnosis')


class Medication(models.Model):
    _patientmedication = models.TextField(
        max_length=5000, blank=True, null=True)
    _patient_non_drug_prescription = models.TextField(
        max_length=5000, blank=True, null=True)
    _patientprogress = models.TextField(max_length=5000, blank=True, null=True)
    _patientdetails = models.ForeignKey(Patient, blank=True, null=True)
    _patientvisit = models.ForeignKey(Visits)
    _patientdiagosis = models.ForeignKey(Diagnosis)

    def __unicode__(self):
        return self._patientmedication

    class Meta:
        verbose_name = _('Patient Medication')
        verbose_name_plural = _('Patient Medications')


class History(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    procedures_performed = models.TextField(1000)
    visit_dates = models.ForeignKey(Visits)
    patient_details = models.ForeignKey(Patient)
    dischage_dates = models.DateField(auto_now=True)
    chief_complaint = models.TextField(max_length=1000)
    dischage_summary = models.TextField(
        max_length=1000, help_text="Please type the dischage summary here .")

    def __unicode__(self):
        return self.diagnosis

    class Meta:
        verbose_name = _('Patient History')
        verbose_name_plural = _('Patient Histories')


class Documents(models.Model):
    patientsdetails = models.ForeignKey(Patient)
    patientsvisit = models.ForeignKey(Visits)
    patients_documents = models.FileField(upload_to='media')

    def __unicode__(self):
        return self.patients_documents

    class Meta:
        verbose_name = _('Patient Document')
        verbose_name_plural = _('Patient Documents')
