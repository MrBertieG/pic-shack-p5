from django import forms
from .models import NewsletterUser


class NewsletterSignupForm (forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = sellf.cleaned_data.get('email')

            return email