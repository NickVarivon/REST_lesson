from django import forms


class PersonsForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    age = forms.IntegerField()
    mail = forms.EmailField()

