# Generated by Django 3.0 on 2020-01-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200115_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comment',
            new_name='is_approved',
        ),
    ]