from django.urls import path

from . import views

urlpatterns = [
    # login user/
    path('<str:username>&<str:password>', views.index, name='index'),
]
