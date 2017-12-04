from django.shortcuts import render
from django.http import HttpResponse
from .models import Dataset
import csv

"""
File: views.py
Modified By: Seungwan Noh
Modifed On: Dec 3, 2017
Description: This view will handle a Web request and returns a Web response. 
"""

class Country:
    """
    This is a class for a country.
    """
    def __init__(self, countryname):
        self.countryname = countryname

    def getCountryName(self):
        return self.countryname

class Province(Country):
    """
    This is a class for a province.
    """
    def __init__(self, countryname, provincename, provinceabbr):
        Country.__init__(self, countryname)
        self.provincename = provincename
        self.provinceabbr = provinceabbr

    def getProvinceName(self):
        return self.provincename

    def getProvinceAbbr(self):
        return self.provinceabbr

# Array to hold of country name, province name, and province abbreviation
canada_province = [
    Province("Canada", "Ontario", "ON"),
    Province("Canada", "Quebec", "QC"),
    Province("Canada", "Nova Scotia", "NS"),
    Province("Canada", "New Brunswick", "NB"),
    Province("Canada", "Manitoba", "MB"),
    Province("Canada", "British Columbia", "BC"),
    Province("Canada", "Prince Edward Island", "PE"),
    Province("Canada", "Saskatchewan", "SK"),
    Province("Canada", "Alberta", "AB"),
    Province("Canada", "Newfoundland and Labrador", "NL"),
]

def convert_province_abbr_to_name(province_abbr):
    # Loop canada_province array
    for cp in canada_province:
        # Check if a province abbreviation is matched.
        if cp.getProvinceAbbr() == province_abbr:
            # Assign a name of province
            province_name = cp.getProvinceName()

    # Return a name of province
    return province_name

def dataloader(request):
    """
    This function is to convert csv data file into database that is sqlite3.
    :param request: http get request
    :return: empty string
    """

    try:
        # Assign a variable by reading a specific csv file.
        data = csv.reader(open("C:\\Users\\wanno\\PycharmProjects\\cst8333\\dataset\\00010014-eng.csv"), delimiter=',')

        # Loop until the last row(line).
        for row in data:

            # Check if this is a field line or not.
            if row[0] != 'Ref_Date':
                dataset = Dataset()

                # Assign each column.
                dataset.ref_date = row[0]
                dataset.geo = row[1]
                dataset.est = row[2]
                dataset.vector = row[3]
                dataset.coordinate = row[4]
                dataset.value = row[5]
                # Save all the assigned data.
                dataset.save()
    # When an error occurred during IO file.
    except IOError:
        print('An error occurred trying to read the file.')

    # Return empty string
    return HttpResponse('')

def get_item_by_province(request):
    """
    This function is to retrieve the matched data from the database.
    :param request: http request
    :return: a matched province value and ajax_filter_table.html
    """

    # Assign province variable from a parameter of GET request.
    province_abbr = request.GET.get('province', None)

    # Assign a name of province from the abbreiviation
    province = convert_province_abbr_to_name(province_abbr)

    context = {
        # Retrieve province data from the database.
        'dataset': Dataset.objects.filter(geo=province)
    }

    # Return data dictionary retrieved to ajax_filter_table.html
    return render(request,'ajax_filter_table.html', context)


def index(request):
    """
    This function will be invoked as a default. As a result, index.html will be open with a default province value.
    :param request: http request
    :return: a default province value and index.html
    """

    # Initial assignment for a province variable
    province = request.GET.get('province', None)

    # Check if province variable is set, otherwise default value would be set to "Canada"
    if province is None:
        province = canada_province.__getitem__(0).getCountryName()

    else:
        print(province)

    context = {
        # Retrieve province data from the database.
        'dataset': Dataset.objects.filter(geo=province)
    }

    # Return data dictionary retrieved to index.html
    return render(request, 'index.html', context)
