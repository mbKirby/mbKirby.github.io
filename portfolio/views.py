import email
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def index(request): 
    form = ContactForm()
    aa = 'aa'
    context = {
    'aa' : aa,
    'form' : form,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message} ')
        emailAndMessage = f'{email} {message}'
        send_mail(
            name,
            emailAndMessage,
            email,
            ['mattswebsite90@gmail.com'],
            fail_silently=False
        )
        return render(request, 'portfolio/index.html', {'name': name})

    return render(request, 'portfolio/index.html', context)