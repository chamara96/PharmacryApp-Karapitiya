# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from firebase import firebase

firebase = firebase.FirebaseApplication("https://pharmacy-test1.firebaseio.com")
data_login = firebase.get('/client_user', '')


def index(request, username, password):
    for i in data_login:
        if (data_login[i]["tele"] == username) and (data_login[i]["password"] == password):
            output = data_login[i]
            break
        else:
            output = {"login": "false"}

    response_login = JsonResponse(output)
    return response_login
