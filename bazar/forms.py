from django import forms
from .models import Polozky

class InzForm(forms.ModelForm):
    class Meta:
        model = Polozky
        fields = ('typ', 'telefon', 'nazev', 'kategorie', 'cena', 'mesto', 'popis', 'image',)
        labels = {
        'typ': 'Typ', 
        'telefon': 'Telefon',
        'nazev': 'Název',
        'kategorie': 'Kategorie',
        'cena': 'Cena',
        'mesto': 'Město',
        'popis': 'Popis',
        'image': 'Obrázek',
        }