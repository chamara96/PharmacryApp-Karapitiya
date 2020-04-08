from django.urls import path

from . import views

urlpatterns = [
    # pharmuser/
    path('', views.index, name='index'),
    # pharmuser/reg/
    path('reg/<str:name>&<str:owner>&<str:tele>&<str:lat>&<str:lng>&<str:address>&<str:password>', views.reg,  name='reg'),
    # view order
    path('vieworder/<str:username>/<str:query>', views.vieworder, name='vieworder'),
    # get order
    path('getorder/<str:username>/<str:orderid>', views.getorder, name='getorder')
]
