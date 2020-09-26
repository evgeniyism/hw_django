import csv
from datetime import datetime
from os.path import dirname, abspath
from .models import Phone
from pprint import pprint

def handle():
    file_name = 'phones.csv'
    path = f'{dirname(dirname(abspath(__file__)))}' + f'\{file_name}'
    with open(path, encoding='UTF8') as file:
        data = csv.DictReader(file, delimiter=';')
        for phone in data:
            date = datetime.strptime(phone['release_date'], '%Y-%m-%d').date()
            new_object = Phone()
            new_object.id = phone['id']
            new_object.name = phone['name']
            new_object.image = phone['image']
            new_object.price = phone['price']
            new_object.date = str(date)
            new_object.lte_exists = phone['lte_exists']
            new_object.slug = phone['name'].replace(' ', '-')
            new_object.save()
