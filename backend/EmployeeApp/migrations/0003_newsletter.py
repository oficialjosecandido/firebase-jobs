# Generated by Django 3.0.7 on 2021-09-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_auto_20210924_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('senderEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Added to the Database', 'Added to the Database'), ('WARNING - ADD TO THE DATABASE', 'WARNING - ADD TO THE DATABASE')], max_length=64)),
            ],
        ),
    ]
