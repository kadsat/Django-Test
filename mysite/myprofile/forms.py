from django.forms import ModelForm,modelformset_factory,forms

from .models import *

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        exclude = ('person',)

class ProfessionForm(ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'
        exclude = ('person',)

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ('person',)
        

VehicleFormSet =  modelformset_factory(Vehicle,fields='__all__')
