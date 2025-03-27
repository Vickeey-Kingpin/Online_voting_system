from django import forms
from .models import Department

class VotersForm(forms.Form):
    fullname = forms.CharField()
    reg_no = forms.CharField()
    departments = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select Your Department")
    stage = forms.CharField()

class VotesForm(forms.Form):
    male_vote = forms.IntegerField(required=False)
    female_vote = forms.IntegerField(required=False)
    academic_vote = forms.IntegerField(required=False)

class StudentRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    reg_no = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

class StudentLoginForm(forms.Form):
    reg_no  = forms.CharField()
    password  = forms.CharField()