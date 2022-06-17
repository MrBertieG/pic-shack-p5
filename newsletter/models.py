from django.db import models

# Create your models here.


class UserNewsletterSub(models.Model):
    """A model for the newsletter subscription"""
    email = models.EmailField(max_length= 250, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
