# Generated by Django 4.0.6 on 2022-07-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_date_added_order_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
