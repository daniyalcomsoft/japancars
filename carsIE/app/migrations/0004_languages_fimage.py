# Generated by Django 3.2.7 on 2021-10-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211004_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='FImage',
            field=models.ImageField(default='', upload_to='productimg', verbose_name='Flag Image'),
            preserve_default=False,
        ),
    ]
