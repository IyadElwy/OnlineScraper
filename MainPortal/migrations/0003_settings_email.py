# Generated by Django 4.0.2 on 2022-02-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPortal', '0002_remove_settings_id_settings_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(default='none@none.com', max_length=254),
            preserve_default=False,
        ),
    ]
