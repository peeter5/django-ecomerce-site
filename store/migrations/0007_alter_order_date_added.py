# Generated by Django 4.0.6 on 2022-07-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_order_date_added_alter_orderitem_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_added',
            field=models.BooleanField(default=False),
        ),
    ]
