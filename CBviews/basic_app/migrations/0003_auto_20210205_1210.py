# Generated by Django 3.1.5 on 2021-02-05 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20210205_1150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='locations',
            new_name='location',
        ),
    ]