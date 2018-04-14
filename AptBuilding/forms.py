from django import forms
from AptBuilding.models import AptBuilding


class AptBuildingForm(forms.ModelForm):

    class Meta:
        model = AptBuilding
        fields = '__all__'
        exclude = ('owner', )
