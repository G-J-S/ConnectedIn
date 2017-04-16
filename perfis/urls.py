from django.conf.urls import url
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar,
                                                    name='convidar'),
    url(r'^convite/(?P<id_convite>\d+)/aceitar$', views.aceitar,
                                                    name='aceitar'),

]
