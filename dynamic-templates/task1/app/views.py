from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    data = csv_reader('G:/PycharmProject/dynamic-templates/task1/inflation_russia.csv')
    context = {'years': data[0:],
               'headers': data[0].keys()
               }
    print ([i for i in data])
    return render(request, template_name,
                  context)


def csv_reader(filepath):
    clean_data = []
    with open(filepath, encoding='UTF-8') as data:
        years = csv.DictReader(data, delimiter=';')
        for year in years:
            to_clean = dict_cleaner(year)
            clean_data.append(to_clean)
    return clean_data


def dict_cleaner(dictionary):
    clean_dict = {}
    for key, value in dictionary.items():
        if value == '':
            value = '-'
        item = {key: value}
        clean_dict.update(item)
    return clean_dict