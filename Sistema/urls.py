from django.conf.urls import url
from django.urls import path
from . import views

# Urls para las Diferentes Paginas
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^registro/$',views.registroPersona,name="registro"),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^olvido/$',views.olvido,name="olvido"),
    url(r'^restablecer/$',views.restablecer,name="restablecer"),
    url(r'^registroPerro/$', views.registroPerro, name='registroPerro'),
    url(r'^registroAdmin/$', views.registroAdmin, name='registroAdmin'),
    url(r'listaPerro/$',views.listaPerro,name="listaPerro"),
    url(r'listaPersona/$',views.listaPersona,name="listaPersona"),
    url(r'^salir/$',views.salir,name="logout"),
]
