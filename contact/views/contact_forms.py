from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact
from contact.forms import ContactForm
# Create your views here.



def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            "form": form
        }

        if form.is_valid():
            form.save()
            return redirect("contact:create")

        
        return render(request,"contact/create.html",context)

    context = {
        "form": ContactForm()
        }
    return render(request,"contact/create.html",context)

