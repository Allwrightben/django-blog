# Generated by Django 4.2.13 on 2024-06-27 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='exerpt',
            new_name='excerpt',
        ),
    ]
