# Generated by Django 3.2 on 2022-06-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220619_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
    ]
