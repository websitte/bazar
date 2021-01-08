from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from bazar.models import Polozky
from django.views import generic

#def index(request):
#   return HttpResponse("Citát pro Homepage <br />Pouze ti, kteří byli natolik naivní, že si mysleli že dokážou změnit svět, ho dokázali opravdu změnit.")

#def index(request): 
#  polozky = Polozky.objects.filter(vytvoreno__lte=timezone.now()).order_by('vytvoreno')
#  return render(request, 'homepage/bazar.html', {'polozky': polozky})

class Index(generic.ListView):
    model = Polozky
    context_object_name = 'zbrane_list'   # your own name for the list as a template variableß
    template_name = 'homepage/bazar.html'  # Specify your own template name/location 

    def get_queryset(self):
        return Polozky.objects.all()
        #return Polozky.objects.filter(nazev__icontains='vzduchov')[:5]
