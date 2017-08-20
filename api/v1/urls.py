from django.conf.urls import url
from . import views

app_name = "v1"

urlpatterns = [ url(r'^$', views.index, name='index'),
                url(r'^v1/create_contacts$', views.create_contacts, name='create_contacts'),
                url(r'^v1/contact$', views.show_contacts, name='contacts'),
                url(r'^v1/contact/(?P<contact_id>[0-9]+)/$', views.contact_edit_page, name='contacts_edit_page'),
                url(r'^v1/edit_contact$', views.edit_contact, name='edit_contact')
                ]