# Generated by Django 3.2.7 on 2023-01-11 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutomerInvoiceDetail',
            fields=[
                ('CIDID', models.AutoField(primary_key=True, serialize=False)),
                ('InvoiceDetail', models.CharField(max_length=200, verbose_name='Invoice Detail')),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.car')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.users')),
            ],
        ),
    ]
