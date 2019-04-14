# Generated by Django 2.0.7 on 2019-03-30 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190312_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useroffice',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='useroffice',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='salesman',
            name='sales_total',
        ),
        migrations.AddField(
            model_name='salesman',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesman',
            name='individual_registration',
            field=models.CharField(blank=True, max_length=14, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='salesman',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Cep'),
        ),
        migrations.AlterField(
            model_name='salesman',
            name='name',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Nome'),
        ),
        migrations.DeleteModel(
            name='UserOffice',
        ),
    ]
