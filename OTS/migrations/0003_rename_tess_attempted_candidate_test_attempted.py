# Generated by Django 4.2.4 on 2023-08-27 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0002_alter_candidate_tess_attempted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='Tess_attempted',
            new_name='test_attempted',
        ),
    ]
