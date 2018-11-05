from django.conf.urls import url
from django.urls import path
from . import views

# Urls para las Diferentes Paginas
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^registro/$',views.registroPersona,name="registro"),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^recover/$',views.recuperar,name="recuperar"),
    url(r'^registroPerro/$', views.registroPerro, name='registroPerro'),
    url(r'^salir/$',views.salir,name="logout"),
]
