# Generated by Django 4.0.6 on 2022-07-29 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.BooleanField(default=False),
        ),
    ]
