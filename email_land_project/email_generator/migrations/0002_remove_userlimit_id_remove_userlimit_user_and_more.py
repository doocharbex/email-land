# Generated by Django 5.0.2 on 2024-04-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlimit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userlimit',
            name='user',
        ),
        migrations.AddField(
            model_name='userlimit',
            name='telegram_id',
            field=models.BigIntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
