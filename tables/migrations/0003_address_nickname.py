# Generated by Django 3.0.4 on 2020-03-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20200311_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='nickname',
            field=models.CharField(default='Home', max_length=50),
            preserve_default=False,
        ),
    ]
