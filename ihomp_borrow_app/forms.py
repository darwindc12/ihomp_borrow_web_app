from django import forms


class BorrowerForm(forms.Form):
    borrower_name = forms.CharField(max_length=80)
    department = forms.CharField(max_length=80)
    category = forms.CharField(max_length=80)
    peripheral = forms.CharField(max_length=80)
    unique_number = forms.CharField(max_length=80)
