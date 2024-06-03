from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = []  # Only include fields you want to be editable by users, excluding 'recommendations'