from django.shortcuts import render, reverse, redirect
from products.models import Product
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):
    """View to return the index page"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'home/index.html', context)


def contact_us(request):
    """ A view to handle the customer contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will \
                be in touch shortly.')
            return redirect(reverse('contact_us'))

    context = {
        'form': form
    }

    return render(request, 'home/contact_us.html', context)

