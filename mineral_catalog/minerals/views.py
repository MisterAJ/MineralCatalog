import re
from django.http import HttpResponse
from django.shortcuts import render

from .models import Mineral

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

CATEGORIES = ['Silicate', 'Oxide', 'Sulfate', 'Sulfide', 'Carbonate',
              'Halide', 'Sulfosalt', 'Phosphate', 'Borate', 
              'Organic Mineral', 'Arsenate', 'Native Element', 'Other']

# Create your views here.

def mineral_list(request):
    """Lists all Minerals"""
    minerals = Mineral.objects.all().values('id', 'name')
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'letters':LETTERS,
                   'categories':CATEGORIES})

def mineral_detail(request, pk):
    """Displays the details of the Mineral"""
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})

def mineral_filter_category(request, filter_term):
    """Lists filtered minerals"""
    minerals = Mineral.objects.all().filter(
        category__contains=filter_term
        ).values('id', 'name')
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'letters':LETTERS,
                   'categories':CATEGORIES,
                   'active':filter_term})

def mineral_filter_name(request, filter_term):
    """Lists filtered by first letter"""
    search = re.escape(filter_term) # make sure there are not regex specials
    minerals = Mineral.objects.all().filter(
        name__iregex=r"(^|\s)%s" % search
        ).values('id', 'name')
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'letters':LETTERS,
                   'categories':CATEGORIES,
                   'active':filter_term})

def mineral_search(request):
    """Lists filtered minerals"""
    search_term = request.POST.get('search')
    minerals = Mineral.objects.all().filter(
        name__contains=search_term
        ).values('id', 'name')
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'letters':LETTERS,
                   'categories':CATEGORIES})
 