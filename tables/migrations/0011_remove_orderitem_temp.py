# Generated by Django 3.0.4 on 2020-04-21 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_orderitem_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='temp',
        ),
    ]
