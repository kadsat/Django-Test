from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    form1 = PersonForm(request.POST or None,initial = {'firstName':'Satiesh','lastName':'R'})
    form2 = LocationForm(request.POST or None,initial = {'firstAddress':'5563','secondAddress':'Spine Rd','city':'Boulder','state':'CO','zip':80301,})
    form3 = ProfessionForm(request.POST or None,initial = {'role':'Developer','companyName':'TCS','industry':'IT'})
    optionalForm = VehicleForm(request.POST or None,initial = {'model':'Murano','year':2016})
    #formSet1 = VehicleFormSet(queryset= Vehicle.objects.none())
    all_forms = [form1,form2,form3,]
    if request.method == 'POST' and all(list(map(lambda _:_.is_valid(),all_forms))) and optionalForm.is_valid():
        person = form1.save()
        forms_without_person = [form2,form3,optionalForm]
        for form in forms_without_person:
            data = form.save(commit=False)
            data.person = person
            data.save()
    return render(request,'myprofile/index.html',{'all_forms':all_forms,'optionalForm':optionalForm})