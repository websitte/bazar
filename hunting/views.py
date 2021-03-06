from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from bazar.models import Polozky
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalLoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'homepage/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('home'))


#def index(request):
#   return HttpResponse("Citát pro Homepage <br />Pouze ti, kteří byli natolik naivní, že si mysleli že dokážou změnit svět, ho dokázali opravdu změnit.")

#def index(request): 
#  polozky = Polozky.objects.filter(vytvoreno__lte=timezone.now()).order_by('vytvoreno')
#  return render(request, 'homepage/bazar.html', {'polozky': polozky})

class Index(generic.ListView):
    paginate_by = 5
    model = Polozky
    context_object_name = 'zbrane_list'   # your own name for the list as a template variableß
    template_name = 'homepage/bazar.html'  # Specify your own template name/location 

    def get_queryset(self):
        return Polozky.objects.all()
        #return Polozky.objects.filter(nazev__icontains='vzduchov')[:5]


class Profil(generic.ListView):
    model = Polozky
    context_object_name = 'profil'   # your own name for the list as a template variableß
    template_name = 'homepage/profil.html'  # Specify your own template name/location 

