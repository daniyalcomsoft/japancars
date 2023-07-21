from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import *
import json

class CompanyForm(forms.ModelForm):
    CompanyName = forms.ModelChoiceField(queryset=Company.objects.values_list('CompanyName', flat=True), label='Select Company')

    class Meta:
        model = Company
        fields = ('CompanyName',)

class CarForm(forms.ModelForm):
    CarName = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    mfdate = models.ForeignKey(ManufacturingYM, on_delete=models.DO_NOTHING)
        

    class Meta:
        model = Car
        fields = ('CarName', 'company', 'mfdate')