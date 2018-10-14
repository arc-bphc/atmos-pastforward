from django import forms


class RegForm(forms.Form):
    team_name = forms.CharField(label="Team Name", max_length="100")
    college_name = forms.CharField(label="College Name", max_length="100")
    email = forms.EmailField()
