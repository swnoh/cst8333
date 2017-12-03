from django.shortcuts import render
from .models import Dataset
import csv


def dataloader():
    data = csv.reader(open("C:\\Users\\wanno\\PycharmProjects\\cst8333\\dataset\\00010014-eng.csv"), delimiter=',')

    for row in data:
        if row[0] != 'Ref_Date':
            dataset = Dataset()

            dataset.ref_date = row[0]
            dataset.geo = row[1]
            dataset.est = row[2]
            dataset.vector = row[3]
            dataset.coordinate = row[4]
            dataset.value = row[5]
            dataset.save()


def get_item_by_province(request):
    """
    View function to handle Ajax request for image Link.
    :param request: Ajax request data.
    :return: image URL.
    """
    # if request.is_ajax():
    #     try:
    #         username = request.POST['username']
    #         # perform operations on the user name.
    #
    #     except:
    #         e = sys.exc_info()
    #         return HttpResponse(e)
    #     return HttpResponse(sucess)
    # else:
    #     raise Http404


    # if request.method == "POST":
    #     selected_province = request.POST['search_text']
    #
    #     context = {
    #         'dataset_ON': Dataset.objects.filter(geo='Ontario'),
    #         'dataset_AB': Dataset.objects.filter(geo='Alberta'),
    #         'dataset_BC': Dataset.objects.filter(geo='British Columbia'),
    #         'dataset_MB': Dataset.objects.filter(geo='Manitoba'),
    #         'dataset_NB': Dataset.objects.filter(geo='New Brunswick'),
    #         'dataset_NL': Dataset.objects.filter(geo='Newfoundland and Labrador'),
    #         'dataset_NS': Dataset.objects.filter(geo='Nova Scotia'),
    #         'dataset_PE': Dataset.objects.filter(geo='Prince Edward Island'),
    #         'dataset_QC': Dataset.objects.filter(geo='Quebec'),
    #         'dataset_SK': Dataset.objects.filter(geo='Saskatchewan'),
    #     }
    province = request.GET.get('province', None)
    context = {
        'dataset': Dataset.objects.filter(geo=province)
    }
    print(context['dataset'])
    return render(request,'ajax_filter_table.html', context)


def index(request):
    # dataloader()
    # context = {
    #     # 'dataset': Dataset.objects.all()
    #     'dataset': Dataset.objects.filter(geo='Canada'),
    # }
    province = request.GET.get('province', None)
    if province == None:
        province = 'Canada'

    context = {
        'dataset': Dataset.objects.filter(geo=province)
    }

    print("index here!!!   ", province)
    return render(request, 'index.html', context)
