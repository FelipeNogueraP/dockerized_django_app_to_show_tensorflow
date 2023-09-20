# Generated by Django 4.2.5 on 2023-09-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='input_data',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='prediction_result',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
