# Generated by Django 3.2.7 on 2021-10-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_shippingsituation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOffice',
            fields=[
                ('SalesOfficeID', models.AutoField(primary_key=True, serialize=False)),
                ('Heading', models.CharField(max_length=200, verbose_name='Heading')),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to='productimg', verbose_name='Contact Image')),
            ],
        ),
    ]
