from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import UserNewsletterSub
from .forms import NewsletterForm

# Create your views here.


def newsletter(request):
    """A view to render the newsletter subscription"""
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if UserNewsletterSub.objects.filter(
                    email=instance.email).exists():
                messages.error(request, 'Email already subscribed')
            else:
                instance.save()
                messages.success(request, 'Thank you for subscribing!')
                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'newsletter.html', context)


def unsub_newsletter(request):
    """ A view to render newsletter unsubscriptions """
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if UserNewsletterSub.objects.filter(
                    email=instance.email).exists():
                UserNewsletterSub.objects.filter(
                    email=instance.email).delete()
                messages.success(request, 'You are no longer a subscriber.')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'This email is not part of our mailing list, please check again.')

    context = {
        'form': form,
    }

    return render(request, 'unsubscribe.html', context)