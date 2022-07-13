from django import forms
from .models import TeamModel


class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamModel
        fields = ['fname','lname','pno','email','role']