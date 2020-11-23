# Generated by Django 3.0.2 on 2020-11-17 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empinfo',
            name='emp_id',
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='managerinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='payment_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 17, 5, 37, 59, 884401, tzinfo=utc), null=True),
        ),
    ]