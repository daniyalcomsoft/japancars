# Generated by Django 3.2.7 on 2021-10-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]