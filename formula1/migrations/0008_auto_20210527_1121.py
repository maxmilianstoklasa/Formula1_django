# Generated by Django 3.2.3 on 2021-05-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0007_auto_20210527_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='teams',
        ),
        migrations.AddField(
            model_name='driver',
            name='teams',
            field=models.ForeignKey(default='', help_text='Select the constructor teams the driver has raced for', on_delete=django.db.models.deletion.CASCADE, to='formula1.constructor'),
        ),
    ]
