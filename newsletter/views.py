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

    return render(request, 'newsletter/newsletter.html', context)