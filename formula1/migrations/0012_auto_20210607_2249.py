# Generated by Django 3.2.3 on 2021-06-07 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0011_auto_20210607_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='teams',
        ),
        migrations.AddField(
            model_name='driver',
            name='teams',
            field=models.ForeignKey(default=3, help_text='Select the constructor team the driver has been racing for', on_delete=django.db.models.deletion.CASCADE, to='formula1.constructor'),
        ),
    ]
