# Generated by Django 4.0.6 on 2022-07-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
