from django.db import models


# Create your models here.
class ContactUs(models.Model):
    """ A Model for the contact form """
    class Meta:
        verbose_name_plural = 'Contact Us'

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=254, null=False, blank=False)