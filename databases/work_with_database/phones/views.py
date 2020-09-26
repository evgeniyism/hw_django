from django.shortcuts import render
from .import_models import handle
from .models import Phone

handle()

def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        all_phones = all_phones.order_by('name')
    if sort == 'min_price':
        all_phones = all_phones.order_by('price')
    if sort == 'max_price':
        all_phones = all_phones.order_by('price').reverse()
    context = {'all_phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    print(phone)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)