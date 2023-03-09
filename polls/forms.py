from django import forms
from .models import Mappin, Mapsdata, Locationadress, Locationdata

class Mappinform(forms.ModelForm):
    class Meta:
        model=Mappin
        fields="__all__"

class Mapsdataform(forms.ModelForm):
    class Meta:
        model=Mapsdata
        fields="__all__"

class Locationadressform(forms.ModelForm):
    class Meta:
        model=Locationadress
        fields="__all__"

class Locationdataform(forms.ModelForm):
    class Meta:
        model=Locationdata
        fields="__all__"