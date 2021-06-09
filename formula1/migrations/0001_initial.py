# Generated by Django 3.2.3 on 2021-05-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a constructor team (Mercedes, McLaren...)', max_length=30, unique=True, verbose_name='Constructor name')),
                ('history', models.TextField(blank=True, null=True, verbose_name='History')),
                ('wins', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of victories')),
                ('championships', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of championships')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
