from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.home),
    path("convert/", include([
        path('<str:type1>/<str:type2>', views.convert),
        re_path(r'^(?P<type1>[\w-]+)\=\>(?P<type2>[\w-]+)$', views.convert),
        re_path(r'^(?P<type2>[\w-]+)\<\=(?P<type1>[\w-]+)$', views.convert),
    ]))
]