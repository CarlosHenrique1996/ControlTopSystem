# Generated by Django 2.1.7 on 2019-03-12 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
        ('accounts', '0003_auto_20190312_0016'),
        ('catalog', '0001_initial'),
        ('salesitem', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalemItem',
            new_name='SalesItem',
        ),
    ]
