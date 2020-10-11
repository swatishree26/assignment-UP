from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

def index(request):
    data=requests.get("http://127.0.0.1:5000/show")
    data = data.text
    data=json.loads(data)
    data=data["food_categories"]
    # a = data.type()
    
    # data=data.slice(0, -1)
    # data=data.substring(1)
    # data = data.text.split(':')
    # data=data[1]
    # data = data.__getitem__(1)
    itemdata=requests.get("http://127.0.0.1:5000/show/1")
    itemdata = itemdata.text
    itemdata=json.loads(itemdata)
    itemdata=itemdata["food_items"]
    return render(request, 'home.html', {'data':data, 'itemdata':itemdata})

    # return render(request, 'home.html', {'data':data})
    # return render(request, 'home.html')

def desc(request, category_id):
    # data=requests.get("your api url")
    data=requests.get("http://127.0.0.1:5000/show")
    data = data.text
    data=json.loads(data)
    data=data["food_categories"]

    itemdata=requests.get("http://127.0.0.1:5000/show/{0}".format(category_id))
    itemdata = itemdata.text
    itemdata=json.loads(itemdata)
    itemdata=itemdata["food_items"]
    return render(request, 'home.html', {'data':data, 'itemdata':itemdata})

# def fooddescription(request):
#     # data=requests.get("your api url")
#     # print(data.html)
#     # data = data.text
#     return render(request, 'home.html', {'data':data})