from django.shortcuts import render
from django.http import HttpResponse
from CRUD_App.models import SampleObject


def index(request):
    list1 = SampleObject.objects.all()
    context = {
        'list1': list1,
    }
    return render(request, 'CRUD_App/index.html', context)


def val(request, key):
    response = "You're looking at the val of key \"" + key +"\":\n\n"
    list1 = SampleObject.objects.all()
    for i in list1:
        if i.key == key:
            response += i.value
    return HttpResponse(response)
