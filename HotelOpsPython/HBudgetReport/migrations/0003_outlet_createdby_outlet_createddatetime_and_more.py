# Generated by Django 4.1.7 on 2023-05-23 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HBudgetReport', '0002_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='CreatedBy',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='outlet',
            name='CreatedDateTime',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='outlet',
            name='IsDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outlet',
            name='ModifyBy',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='outlet',
            name='ModifyDateTime',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='outlet',
            name='OrganizationID',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]