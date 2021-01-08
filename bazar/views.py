from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import KategorieBazaru, Polozky
from django.views import generic


#def index(request):
#    return HttpResponse("BAZAR - Pouze ti, kteří byli natolik naivní, že si mysleli že dokážou změnit svět, ho dokázali opravdu změnit.")

class Zbrane(generic.ListView):
    model = Polozky
    context_object_name = 'zbrane_list'   # your own name for the list as a template variableß
    template_name = 'homepage/bazar.html'  # Specify your own template name/location 

    def get_queryset(self):
        return Polozky.objects.all()
        #return Polozky.objects.filter(nazev__icontains='vzduchov')[:5]