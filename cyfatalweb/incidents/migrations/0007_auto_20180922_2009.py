# Generated by Django 2.0.8 on 2018-09-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0006_incidentsource_source_candidate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='coordinates',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='motorist_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='motorist_gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='motorist_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='state',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='vehicle_make',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='vehicle_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='victim_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='victim_gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='victim_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='incidentsource',
            name='article_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incidentsource',
            name='article_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incidentsource',
            name='domain',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='incidentsource',
            name='site_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
