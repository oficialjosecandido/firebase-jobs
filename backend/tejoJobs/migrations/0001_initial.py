# Generated by Django 3.0.7 on 2021-12-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('senderName', models.CharField(blank=True, max_length=100, null=True)),
                ('senderEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('senderMessage', models.TextField(blank=True, null=True)),
                ('senderSKU', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Unread', 'Unread')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
                ('DepartmentImage', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField(auto_now_add=True)),
                ('PhotoFileName', models.CharField(max_length=100)),
                ('Email', models.CharField(blank=True, max_length=150, null=True)),
                ('Bio', models.TextField(blank=True, null=True)),
                ('Primary_Tech', models.CharField(blank=True, max_length=100, null=True)),
                ('Primary_Tech_Experience', models.CharField(blank=True, max_length=100, null=True)),
                ('Working', models.CharField(blank=True, max_length=100, null=True)),
                ('Expected_Sallary', models.IntegerField(blank=True, default=100, null=True)),
                ('Location', models.CharField(blank=True, max_length=300, null=True)),
                ('Remote', models.BooleanField(blank=True, default=False, null=True)),
                ('soft_report', models.BooleanField(blank=True, default=False, null=True)),
                ('tech_report', models.BooleanField(blank=True, default=False, null=True)),
                ('WorkExperience1_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience1_startYear', models.IntegerField(blank=True, default=2000, null=True)),
                ('WorkExperience1_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience1_endYear', models.IntegerField(blank=True, default=2000, null=True)),
                ('WorkExperience1_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience1_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience1_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience1_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience1_description', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience2_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience2_startYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience2_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience2_endYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience2_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience2_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience2_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience2_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience2_description', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience3_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience3_startYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience3_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience3_endYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience3_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience3_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience3_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience3_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience3_description', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience4_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience4_startYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience4_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience4_endYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience4_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience4_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience4_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience4_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience4_description', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience5_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience5_startYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience5_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience5_endYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience5_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience5_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience5_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience5_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience5_description', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience6_title', models.CharField(blank=True, max_length=100, null=True)),
                ('WorkExperience6_startYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience6_startMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience6_endYear', models.IntegerField(blank=True, null=True)),
                ('WorkExperience6_endMonth', models.CharField(blank=True, max_length=12, null=True)),
                ('WorkExperience6_techs', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience6_company', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience6_companyLink', models.CharField(blank=True, max_length=300, null=True)),
                ('WorkExperience6_description', models.CharField(blank=True, max_length=300, null=True)),
                ('tech1', models.CharField(blank=True, max_length=100, null=True)),
                ('tech1_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech1_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech2', models.CharField(blank=True, max_length=100, null=True)),
                ('tech2_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech2_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech3', models.CharField(blank=True, max_length=100, null=True)),
                ('tech3_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech3_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech4', models.CharField(blank=True, max_length=100, null=True)),
                ('tech4_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech4_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech5', models.CharField(blank=True, max_length=100, null=True)),
                ('tech5_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech5_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech6', models.CharField(blank=True, max_length=100, null=True)),
                ('tech6_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech6_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech7', models.CharField(blank=True, max_length=100, null=True)),
                ('tech7_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech7_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('tech8', models.CharField(blank=True, max_length=100, null=True)),
                ('tech8_version', models.CharField(blank=True, max_length=100, null=True)),
                ('tech8_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('language1', models.CharField(blank=True, max_length=150, null=True)),
                ('language1_level', models.CharField(blank=True, max_length=150, null=True)),
                ('language2', models.CharField(blank=True, max_length=150, null=True)),
                ('language2_level', models.CharField(blank=True, max_length=150, null=True)),
                ('language3', models.CharField(blank=True, max_length=150, null=True)),
                ('language3_level', models.CharField(blank=True, max_length=150, null=True)),
                ('language4', models.CharField(blank=True, max_length=150, null=True)),
                ('language4_level', models.CharField(blank=True, max_length=150, null=True)),
                ('language5', models.CharField(blank=True, max_length=150, null=True)),
                ('language5_level', models.CharField(blank=True, max_length=150, null=True)),
                ('github', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio', models.CharField(blank=True, max_length=100, null=True)),
                ('Views', models.IntegerField(blank=True, default=0, null=True)),
                ('Rating', models.IntegerField(blank=True, default=0, null=True)),
                ('Featured', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageId', models.AutoField(primary_key=True, serialize=False)),
                ('senderName', models.CharField(max_length=100)),
                ('senderEmail', models.CharField(max_length=100)),
                ('receiverName', models.CharField(max_length=100)),
                ('receiverEmail', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('sendDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Read', 'Read'), ('Unread', 'Unread'), ('Archive', 'Archive')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('senderEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Added to the Database', 'Added to the Database'), ('WARNING - ADD TO THE DATABASE', 'WARNING - ADD TO THE DATABASE')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SoftReport',
            fields=[
                ('SoftReportId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeId', models.CharField(max_length=100)),
                ('softName', models.CharField(max_length=300)),
                ('softEmail', models.CharField(max_length=300)),
                ('softCompany', models.CharField(blank=True, max_length=300, null=True)),
                ('softVAT', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Unread', 'Unread')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('TechId', models.AutoField(primary_key=True, serialize=False)),
                ('TechName', models.CharField(max_length=100)),
                ('TechImage', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TechReport',
            fields=[
                ('TechReportId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeId', models.CharField(max_length=100)),
                ('techName', models.CharField(max_length=300)),
                ('techEmail', models.CharField(max_length=300)),
                ('techCompany', models.CharField(blank=True, max_length=300, null=True)),
                ('techVAT', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Unread', 'Unread')], max_length=64)),
            ],
        ),
    ]
