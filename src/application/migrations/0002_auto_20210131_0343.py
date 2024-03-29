# Generated by Django 3.1.4 on 2021-01-30 22:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='small description of this task 25-100 characters', max_length=1000)),
                ('detailed_description', ckeditor.fields.RichTextField(blank=True, help_text='Here you can define task details rules and all other possible requirements', null=True)),
                ('start_time', models.DateTimeField(help_text='Start date and time of the task format must be YYYY-MM-DD')),
                ('end_time', models.DateTimeField(help_text='End date and time of the task format must be YYYY-MM-DD')),
                ('is_active', models.BooleanField(default=True, help_text='If you check this it means the task is active and if you disable it it will be removed temporary')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text='End date and time of the task')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employees'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Date of Birth - Format must be YYYY-MM-DD', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, help_text='Complete address within area/street, city state and country etc.', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact_no',
            field=models.CharField(blank=True, help_text='employee phone or landline number', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joined_on',
            field=models.DateField(blank=True, help_text='Date of Joining - Format must be YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nic',
            field=models.CharField(blank=True, help_text='National Identification Card or ID card', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='org_id',
            field=models.CharField(blank=True, help_text='Organizational Registration Number or ID', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rank',
            field=models.CharField(blank=True, choices=[('CEO', 'Chief Executive Officer'), ('DIR', 'Director'), ('MAN', 'Manager'), ('WOR', 'Worker'), ('OTH', 'Other')], help_text='Employee Rank/Post/Destination within organization', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
