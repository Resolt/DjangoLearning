# Generated by Django 3.0 on 2020-01-15 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='appr_comment',
            new_name='approved_comment',
        ),
    ]
