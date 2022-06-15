from django.shortcuts import render
from .models import NewsletterUser
from .forms import NewsletterSignupForm

# Create your views here.


def newsletter_signup(request):
    """A vew to render the email form"""
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("email already exists")
        else:
            instance.save()
    
    context = {
        'form': form,
    }
    template = "base.html"

    return render(request, template, context)

# Unsubscribe


def newsletter_unsubscribe(request):
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
        else:
            print('Sorry, no email found')

    context = {
        'form': form,
    }
    template = "templates/base.html"
        
    return render(request, template, context)