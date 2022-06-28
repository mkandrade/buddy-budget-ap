from django import forms


class ExpensesForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()
