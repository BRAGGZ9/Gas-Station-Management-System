# Generated by Django 4.0.3 on 2022-04-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmsApp', '0003_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
