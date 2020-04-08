from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from firebase import firebase

import requests
import json

import datetime
now = datetime.datetime.now()
create_date=now.strftime("%Y-%m-%d %H:%M:%S")

firebase = firebase.FirebaseApplication('https://pharmacy-test1.firebaseio.com/', None)


def index(request):
    return HttpResponse("Hello, world. Home Index of Client Registation")

def clientsetorder(request, username,pharmlist):
    pharm_list = pharmlist.split(",")
    selected_pharm = "none"
    status = "none"

    data_order = {
                'order_id': '',
                'pharm_ids': pharm_list,
                'client_id': username,
                'selected_pharm': selected_pharm,
                'states': status,
                'date_create': create_date,
                'update':''
                }

    result = firebase.post('/orders/', data_order)
    firebase.put('/orders/' + result["name"], 'order_id', result["name"])
    succsess = firebase.get('/orders/' + result["name"], '')
    response_setorder = JsonResponse(succsess)

    return response_setorder

def get_near_locations(username, lat_user, lng_user):
    succsess = firebase.get('/pharm_user/', '')

    mydistrict = "kegalle"
    pharm_id = []
    g_map_destination = ""
    for j in succsess:
        if succsess[j]["district"] == mydistrict:
            pharm_id.append(succsess[j]["id"])
            lat = str(succsess[j]["lat"])
            lng = str(succsess[j]["lng"])
            g_map_destination += "%7C" + lat + "%2C" + lng

    # print(pharm_id)

    final_g_map_dest = g_map_destination[3:]
    # final_g_map_dest = "7.294681%2C80.631272"
    # lat="7.294246"
    # lng="80.626552"
    # print(final_g_map_dest)
    # ------------------------

    g_map_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + lat_user + "," + lng_user + "&destinations=" + final_g_map_dest + "&key=AIzaSyAdnXu5TE8yzZDBaneprA857VAuYnjsC8k"

    json_distance = requests.get(g_map_url)

    row_distance = json.loads(json_distance.text)

    pharmacy_distance = row_distance["rows"][0]["elements"]
    pharmacy_address_gmap=row_distance["destination_addresses"]
    origin_address=row_distance["origin_addresses"]

    phar_list = []
    for i, k, q in zip(pharmacy_distance, pharm_id, pharmacy_address_gmap):
        # temp = [{'pharm_id': k}, {'distance': i["distance"]["value"]}, {'time': i["duration"]["text"]},{'destination_addresses': q}]
        temp = {"pharm_id": k, "distance": i["distance"]["value"], "time": i["duration"]["text"], "destination_addresses": q}
        phar_list.append(temp)

    # sorted_phar_list = sorted(phar_list, key=lambda x: x[1]['distance'])
    sorted_phar_list = sorted(phar_list, key=lambda x: x['distance'])
    # sorted_phar_list=[{'pharm_id': '004', 'distance': '1501', 'time': '5 mins', 'destination_addresses': '60 Sri Dalada Veediya, Kandy, Sri Lanka'}, {'pharm_id': '003', 'distance': '1869', 'time': '7 mins', 'destination_addresses': '41, 1 Sri Pushpadana Mawatha, Kandy, Sri Lanka'}, {'pharm_id': '002', 'distance': '2708', 'time': '10 mins', 'destination_addresses': '41 A9, Kandy 20000, Sri Lanka'}, {'pharm_id': '001', 'distance': '3910', 'time': '10 mins', 'destination_addresses': 'Department Office, A1, Kandy, Sri Lanka'}]
    # print(sorted_phar_list)
    # my_json_string = json.dumps(sorted_phar_list)
    # ///////////////////////
    # data_pharm = {sorted_phar_list
    #               }
    data_pharm = {'data': sorted_phar_list,
                  'username': username,
                  'origin_address':origin_address
                  }

    return data_pharm


def pharmlocations(request, username, lat_user, lng_user):
    user_details = firebase.get('/client_user', '')
    for i in user_details:
        if user_details[i]["tele"] == username:
            data_login = get_near_locations(username, lat_user, lng_user)
            break
        else:
            data_login = {"login": "false"}

    response_login = JsonResponse(data_login)
    return response_login


def reg(request, name, tele, lat, lng, address, password):
    data_reg = {'id': '',
                'name': name,
                'tele': tele,
                'address': address,
                'lat': lat,
                'lng': lng,
                'password': password
                }

    result = firebase.post('/client_user/', data_reg)
    firebase.put('/client_user/' + result["name"], 'id', result["name"])
    succsess = firebase.get('/client_user/' + result["name"], '')
    response_reg = JsonResponse(succsess)
    return response_reg
