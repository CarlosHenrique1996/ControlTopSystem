# Generated by Django 2.0.7 on 2019-04-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190331_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='warranty',
            field=models.PositiveIntegerField(default=1, verbose_name='Garantia'),
        ),
    ]
