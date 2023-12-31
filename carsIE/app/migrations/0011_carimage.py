# Generated by Django 3.2.7 on 2021-10-15 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211014_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('CarImageID', models.AutoField(primary_key=True, serialize=False)),
                ('CarImage', models.ImageField(upload_to='productimg', verbose_name='Vehicle Image')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.car', verbose_name='Car')),
            ],
        ),
    ]
