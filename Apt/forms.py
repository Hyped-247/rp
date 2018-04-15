from django import forms

from Apt.models import Apt
from AptBuilding.models import AptBuilding


class AptForm(forms.ModelForm):
    class Meta:
        model = Apt
        fields = '__all__'
        exclude = ('aptBuilding', )
