# Generated by Django 2.2 on 2020-06-30 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200630_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcustomer',
            old_name='cutomer_address',
            new_name='customer_address',
        ),
    ]
