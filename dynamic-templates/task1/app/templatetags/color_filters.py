from django.template import library
register = library.Library()

YEARS = [i for i in range(1991,2019)]

@register.filter
def get_color(value):
    if value == '-':
        return 'white'

    check = float(value)
    if check < 0:
        return 'green'
    elif 0 < check < 1:
        return 'white'
    else:
        if  1 < check < 2:
            return '#E9967A'
        if 2 < check < 5:
            return '#CD5C5C'
        else:
            return '#B22222'
