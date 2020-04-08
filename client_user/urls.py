from django.urls import path

from . import views

urlpatterns = [
    # clientuser/
    path('', views.index, name='index'),
    # clientuser/reg/
    path('reg/<str:name>&<str:tele>&<str:lat>&<str:lng>&<str:address>&<str:password>', views.reg, name='reg'),
    # clientuser/
    # path('login/<str:username>&<str:password>', views.login, name='login'),
    path('pharmlist/<str:username>/<str:lat_user>&<str:lng_user>', views.pharmlocations, name='pharmlocations'),
    # client set order
    path('setorder/<str:username>/<str:pharmlist>', views.clientsetorder, name='clientsetorder'),

]
