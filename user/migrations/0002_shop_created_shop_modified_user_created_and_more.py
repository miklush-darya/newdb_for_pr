# Generated by Django 4.0.6 on 2022-07-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='shop',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Created'),
        ),
    ]
