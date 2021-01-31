from django.contrib import admin
from .models import Polozky, KategorieBazaru, TypInzeratu


@admin.register(TypInzeratu)
class TypInzeratuAdmin(admin.ModelAdmin):
    list_display = ['nazev']

admin.site.register(KategorieBazaru)

@admin.register(Polozky)
class PolozkaBazaruAdmin(admin.ModelAdmin):
    list_display = ['typ','kategorie', 'nazev', 'autor','telefon', 'mesto', 'cena']
    list_filter = ['typ','kategorie', 'autor', 'mesto']
    search_fields = ['nazev']
