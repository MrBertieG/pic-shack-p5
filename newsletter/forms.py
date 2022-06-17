from django import forms
from .models import UserNewsletterSub


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = UserNewsletterSub
        fields = ['email',]