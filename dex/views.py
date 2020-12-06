from django.http.response import HttpResponse, HttpResponseRedirect
from operator import attrgetter
from django.shortcuts import render
from django.urls import reverse
from dex.models import Contact
from .forms import NewContactForm
from .filters import ContactFilter

# Create your views here.
def index(request):

    # contacts = sorted(Contact.objects.all(), key=attrgetter('updated_at'), reverse=True)
    contacts = Contact.objects.all()

    myFilter = ContactFilter(request.GET, queryset=contacts)
    contacts = myFilter.qs
    
    context = {"contacts": contacts, "myFilter": myFilter}

    return render(request, 'index.html', context)


def add(request):
    if request.method == "POST": 
        form_data = NewContactForm(request.POST, request.FILES) 
        if form_data.is_valid():  
            contact_name = form_data.cleaned_data['contact_name']
            email = form_data.cleaned_data['email']
            contact = form_data.cleaned_data['contact']
            # new Contact(request.body)
            contact_info = Contact(contact_name=contact_name, email=email, contact=contact,)
            contact_info.save()  
            return HttpResponseRedirect(reverse("index"))
        else: 
            return HttpResponseRedirect(reverse("add"))  

    return render(request, 'add.html', {"form": NewContactForm()})

def delete_contact(request, id):
    contact = Contact.objects.get(pk=id)
    # localhost:8000/show/id?del=true
    if request.GET.get("del") == "true":
        contact.delete()  # deletes on cat
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'index.html', {"contact": contact})

def update_contact(request, id):
    contact = Contact.objects.get(pk=id)

    if request.method == "POST":
        form_data = NewContactForm(request.POST, request.FILES, instance=contact)  # django
        if form_data.is_valid():  # django
            form_data.save()  # save data to db
            # particular page
            # redirect to the page with the id
            #  the "," at the end is part of the code
            return HttpResponseRedirect(reverse("index"))

    form = NewContactForm(instance=contact)

    return render(request, 'update.html', {"contact": contact, "form": form})
    