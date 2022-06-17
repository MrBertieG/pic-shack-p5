from django.contrib import admin
from .models import UserNewsletterSub

# Register your models here.


class SubAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date',)

    search_fields = ('email', 'date',)


admin.site.register(UserNewsletterSub, SubAdmin)