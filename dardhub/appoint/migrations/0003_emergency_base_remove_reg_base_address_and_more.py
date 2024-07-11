# Generated by Django 5.0.6 on 2024-06-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0002_reg_base_address_reg_base_contact_reg_base_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_local', models.CharField(blank=True, max_length=200, null=True)),
                ('relation_local', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_local', models.CharField(blank=True, max_length=200, null=True)),
                ('address_local', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reg_base',
            name='address',
        ),
        migrations.RemoveField(
            model_name='reg_base',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='reg_base',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reg_base',
            name='relation',
        ),
    ]
