# Generated by Django 4.2.10 on 2024-02-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_userdetails_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='key',
        ),
    ]
