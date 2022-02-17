from django import forms
from .models import *

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
