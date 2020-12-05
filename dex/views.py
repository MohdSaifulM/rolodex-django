from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from dex.models import Contact
from .forms import NewContactForm

# Create your views here.
def index(request):
    contacts = Contact.objects.all()

    return render(request, 'index.html', {"contacts": contacts})

def add(request):
    if request.method == "POST": 
        form_data = NewContactForm(request.POST) 
        if form_data.is_valid():  
            name = form_data.cleaned_data['name']
            email = form_data.cleaned_data['email']
            contact = form_data.cleaned_data['contact']
            # image_url = form_data.cleaned_data['image_url']
            # new Contact(request.body)
            contact_info = Contact(name=name, email=email, contact=contact)
            
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
        form_data = NewContactForm(request.POST, instance=contact)  # django
        if form_data.is_valid():  # django
            form_data.save()  # save data to db
            # particular page
            # redirect to the page with the id
            #  the "," at the end is part of the code
            return HttpResponseRedirect(reverse("index"))

    form = NewContactForm(instance=contact)

    return render(request, 'update.html', {"contact": contact, "form": form})