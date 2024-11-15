# app/forms.py
from django import forms
from .models import Income, Expense

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'description', 'date']

