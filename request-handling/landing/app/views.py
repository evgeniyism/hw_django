from collections import Counter

from django.http import Http404
from django.shortcuts import render

# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    source = request.GET.get('from-landing')
    if source == 'original':
        counter_click['original'] += 1
    if source == 'test':
        counter_click['test'] += 1
    return render(None, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    version = request.GET.get('ab-test-arg')
    if version == 'original':
        counter_show['original'] += 1
        return render(None, 'landing.html')
    if version == 'test':
        counter_show['test'] += 1
        return landing_alternate(request)
    else:
        raise Http404


def landing_alternate(request):
    return render(None, 'landing_alternate.html')


def conversion(version: str):
    conversion = counter_click[version] / counter_show[version]
    return conversion


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(None, 'stats.html', context={
        'test_conversion': conversion('test'),
        'original_conversion': conversion('original'),
    })
