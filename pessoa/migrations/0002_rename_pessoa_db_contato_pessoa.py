# Generated by Django 4.1.1 on 2022-10-04 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='pessoa_db',
            new_name='pessoa',
        ),
    ]
