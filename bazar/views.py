from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import KategorieBazaru, Polozky
from django.views import generic
from .forms import InzForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

#def index(request): 
#  polozky = Polozky.objects.filter(vytvoreno__lte=timezone.now()).order_by('vytvoreno')
#  return render(request, 'homepage/bazar.html', {'polozky': polozky})


# detail inzerátu
def inz_detail(request, pk):
    polozka = get_object_or_404(Polozky, pk=pk)
    return render(request, 'homepage/inz_detail.html', {'polozka': polozka})


# list pouze uživatelových inzerátů
def inz_user(request): 
    logged_in_user = request.user
    logged_in_user_posts = Polozky.objects.filter(autor=logged_in_user)
    return render(request, 'homepage/bazar.html', {'zbrane_list': logged_in_user_posts})


@login_required
def inz_new(request):
    if request.method == "POST":
        form = InzForm(request.POST)
        if form.is_valid():
            inz = form.save(commit=False)
            inz.autor = request.user
            inz.publikovano = timezone.now()
            inz.save()
            return redirect('inz_detail', pk=inz.pk)
    else:
        form = InzForm()
        return render(request, 'homepage/inz_edit.html', {'form': form})


@login_required
def inz_edit(request, pk):
    inz = get_object_or_404(Polozky, pk=pk)
    if request.method == "POST":
        form = InzForm(request.POST, instance=inz)
        if form.is_valid():
            inz = form.save(commit=False)
            inz.autor = request.user
            inz.publikovano = timezone.now()
            inz.save()
            return redirect('inz_detail', pk=inz.pk)
    else:
        form = InzForm(instance=inz)
        return render(request, 'homepage/inz_edit.html', {'form': form})