# Generated by Django 2.2 on 2020-06-30 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allcustomer',
            old_name='cutomer_id',
            new_name='customer_id',
        ),
    ]
