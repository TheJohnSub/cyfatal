# Generated by Django 2.0.8 on 2019-09-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0007_auto_20180922_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incidentsource',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
