from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from firebase import firebase

import requests
import json

import datetime
now = datetime.datetime.now()
update_date=now.strftime("%Y-%m-%d %H:%M:%S")

firebase = firebase.FirebaseApplication('https://pharmacy-test1.firebaseio.com/', None)


# firebase = firebase.FirebaseApplication("https://pharmacy-test1.firebaseio.com")


def index(request):
    return HttpResponse("Hello, world. Home Index of Pharm Registation")


def reg(request, name, owner, tele, lat, lng, address, password):
    data_reg = {'id': '',
                'name': name,
                'owner': owner,
                'tele': tele,
                'address': address,
                'lat': lat,
                'lng': lng,
                'password': password
                }

    result = firebase.post('/pharm_user/', data_reg)
    firebase.put('/pharm_user/' + result["name"], 'id', result["name"])
    succsess = firebase.get('/pharm_user/' + result["name"], '')
    response_reg = JsonResponse(succsess)
    return response_reg


def vieworder(request, username, query):
    data_order = firebase.get('/orders', '')
    view_order = []
    for z in data_order:
        if username in data_order[z]['pharm_ids']:
            temp = data_order[z]
            view_order.append(temp)

    output_order = {
        'orders_list': view_order,
        'username': username
    }
    # response_vieworder = json.dumps(output_order)
    response_vieworder = JsonResponse(output_order)
    return response_vieworder
    # return HttpResponse("Hello, world. Home Index of Pharm Registation")


def getorder(request,username,orderid):
    firebase.put('/orders/' + orderid , 'selected_pharm', username)
    firebase.put('/orders/' + orderid, 'update', update_date)
    
    succsess = firebase.get('/orders/' + orderid, '')
    response_reg = JsonResponse(succsess)
    return response_reg
    # return HttpResponse("Hello, world. Home Index of get order Registation")
