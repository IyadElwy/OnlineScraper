# Generated by Django 4.0.2 on 2022-02-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPortal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='id',
        ),
        migrations.AddField(
            model_name='settings',
            name='p',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]