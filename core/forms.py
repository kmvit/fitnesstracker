from django import forms
from core.models import EveryDayReport, EveryWeekReport


class EveryDayReportForm(forms.ModelForm):
    class Meta:
        model = EveryDayReport
        fields = ['date', 'weight', 'steps', 'critical_days', 'link', 'file']
        widgets = {
            'date': forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'})
        }


class EveryWeekReportForm(forms.ModelForm):
    class Meta:
        model = EveryWeekReport
        fields = ['date', 'weight', 'neck', 'waist', 'hips', 'side_view', 'back_view', 'front_view']
        widgets = {
            'date': forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'})
        }