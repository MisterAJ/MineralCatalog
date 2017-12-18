from django.http import HttpResponse
from django.shortcuts import render

from .models import Mineral


# Create your views here.


def mineral_list(request):
    """Lists all Minerals"""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Displays the details of the Mineral"""
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
