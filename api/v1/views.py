from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def show_contacts(request):
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'v1/contacts.html', context)

def create_contacts(request):

    new_name = request.POST['name']
    new_msisdn = request.POST['msisdn']
    new_address = request.POST['address']

    if(new_name == "name" or new_msisdn == "Contact Number" or new_address == "address"):
        contacts = Contacts.objects.all()
        context = {'contacts': contacts,
                   'error_message': "Not valid input"}
        return render(request, 'v1/contacts.html', context)
    else:
        c = Contacts(name = new_name, msisdn = new_msisdn, address = new_address)
        c.save()
        contacts = Contacts.objects.all()
        context = {'contacts': contacts,
                   'success_message': "Successfully Submitted Data"}
        return render(request, 'v1/contacts.html', context)