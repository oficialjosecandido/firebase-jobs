# Generated by Django 3.0.7 on 2021-09-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language1_level',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language2_level',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language3',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language3_level',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language4',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language4_level',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language5',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='language5_level',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
