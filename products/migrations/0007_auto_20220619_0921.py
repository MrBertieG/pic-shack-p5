# Generated by Django 3.2 on 2022-06-19 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0006_alter_review_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 - Will not recommend'), (2, '1 - Could be beter'), (3, "1 - It's ok"), (4, '1 - I love it!')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='profiles.userprofile'),
        ),
    ]
