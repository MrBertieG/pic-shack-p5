# Generated by Django 3.2 on 2022-06-19 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_review_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on']},
        ),
    ]