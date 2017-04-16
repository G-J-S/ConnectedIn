from django.conf.urls import url
from usuarios import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^registrar$', views.RegistrarUsuarioView.as_view(),
        name="registrar"),
    url(r'^login/$', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, { 'login_url': '/login/' },
        name='logout')
]
