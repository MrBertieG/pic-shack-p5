from django.contrib import admin
from .models import NewsletterUser

# Register your models here.


class NewsLetterAdmin(admin.ModelAdmin):
    """A view to render the emails"""
    list_display = ('email', 'date_signup',)


admin.site.register(NewsletterUser, NewsLetterAdmin)