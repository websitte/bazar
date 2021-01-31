from django.db import models
from django.utils import timezone
#from ckeditor.fields import RichTextField


class Polozky(models.Model):
    typ = models.ForeignKey('TypInzeratu', null=True, on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    telefon = models.CharField(max_length=200, blank=True, null=True)
    nazev = models.CharField(max_length=200)
    kategorie = models.ForeignKey('KategorieBazaru', null=True, on_delete=models.CASCADE)
    cena = models.CharField(max_length=200)
    mesto = models.CharField(max_length=50)
    popis = models.TextField()
    #popis = RichTextField()
    image = models.ImageField(upload_to='static/fotoinzerce/%Y/%m/%d',null=True,blank=True)
    vytvoreno = models.DateTimeField(default=timezone.now)
    publikovano = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazev           # vrati nazev pro admin

    class Meta:
        verbose_name = 'Inzerát'
        verbose_name_plural = 'Inzeráty'


class TypInzeratu(models.Model):
    nazev = models.CharField(max_length=200,
    choices= [             
            ('Prodám', 'Prodám'), 
            ('Koupím', 'Koupím'),     
        ]    
    
    )
    def __str__(self):
        return self.nazev

    class Meta:
        verbose_name = 'Typ inzerátu'
        verbose_name_plural = 'Typ inzerátu'


class KategorieBazaru(models.Model):
    nazev = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nazev

    class Meta:
        verbose_name = 'Kategorie bazaru'
        verbose_name_plural = 'Kategorie bazaru'