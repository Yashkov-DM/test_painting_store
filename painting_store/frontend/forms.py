from django import forms


class StoreForm(forms.Form):
    title = forms.CharField(max_length=50)
    year = forms.CharField(max_length=4)

