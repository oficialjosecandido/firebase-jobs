# Generated by Django 3.0.7 on 2021-10-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0008_softreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='Featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
