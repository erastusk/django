from django.shortcuts import render, redirect
from django.middleware.csrf import get_token
from .forms import ContactForm

# Create your views here.
def contact(request):
    csrf_token = get_token(request)    
    form = ContactForm()    
    return render(request, 'contact/contact.html', {'form':form})
