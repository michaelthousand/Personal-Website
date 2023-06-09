from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here


def home(request):
    return render(request, 'mainsite/home.html')

def about(request):
    return render(request, 'mainsite/about.html')

def projects(request):
    return render(request, 'mainsite/projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'michael.w.thousand@gmail.com', ['michael.w.thousand@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contactsuccess")
    else:
        form = ContactForm()
    return render(request, "mainsite/contact.html", {'form': form})

def contactsuccess(request):
    return render(request, 'mainsite/contactsuccess.html')