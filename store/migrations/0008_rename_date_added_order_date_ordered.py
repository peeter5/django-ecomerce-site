# Generated by Django 4.0.6 on 2022-07-29 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_added',
            new_name='date_ordered',
        ),
    ]
