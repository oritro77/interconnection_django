from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
# Create your views here.
#for testing routes
def index(request):
    return HttpResponse("Hello world")

#view for showing the contacts
def show_contacts(request):
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'v1/contacts.html', context)

#view for creating a contact
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

#view for showing the contacts edit page
def contact_edit_page(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    context = {'contact': contact}
    return render(request, 'v1/edit_contacts.html', context)

#view for editing the contacts
def edit_contact(request):
    if request.POST.get("edit"):
        contact_id = int(request.POST["id"])
        new_name = request.POST["name"]
        new_msisdn = request.POST["msisdn"]
        new_address = request.POST["address"]
        contact = Contacts.objects.get(id=contact_id)

        contact.name = new_name
        contact.address = new_address
        contact.msisdn = new_msisdn

        contact.save()

        return HttpResponse("Contact has been edited")
    elif request.POST.get("delete"):
        contact_id = int(request.POST["id"])
        contact = Contacts.objects.get(id=contact_id)
        contact.delete()
        return HttpResponse("Contact has been deleted")
    elif request.POST.get("back"):
        return show_contacts(request)