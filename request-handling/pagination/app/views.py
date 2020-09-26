from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator
from django.http import HttpResponse

def index(request):
    return redirect(reverse(bus_stations))

def read_csv(file):
    clean_dict = []
    with open(file, encoding='cp1251') as data:
        stations = csv.DictReader(data)
        for row in stations:
            clean = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            clean_dict.append(clean)
    return clean_dict

def bus_stations(request):
    data = read_csv(settings.BUS_STATION_CSV)
    paginator = Paginator(data, 10)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(current_page)
    next, previous = None, None
    if page_obj.has_next():
        next = page_obj.next_page_number()
    if page_obj.has_previous():
        previous = page_obj.previous_page_number()
    context = {
        'bus_stations': page_obj,
        'current_page': page_obj.number,
        'prev_page_url': f'bus_stations?page={previous}',
        'next_page_url': f'bus_stations?page={next}'
    }
    return render(request, 'index.html', context=context)