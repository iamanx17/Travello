from django import forms
from .models import userdata

class user(forms.ModelForm):

    class Meta:
        model=userdata
        fields="__all__"