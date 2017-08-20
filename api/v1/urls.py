from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [ url(r'^$', views.index, name='index'),
                url(r'^v1/create_contacts$', views.create_contacts, name='create_contacts'),
                url(r'^v1/contact$', views.show_contacts, name='contacts'),]