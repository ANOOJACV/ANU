# Generated by Django 4.1.5 on 2023-01-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_alter_branch_district_alter_branch_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
