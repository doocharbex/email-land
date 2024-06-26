# Generated by Django 5.0.2 on 2024-04-05 06:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_generator', '0002_remove_userlimit_id_remove_userlimit_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userlimit',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlimit',
            name='telegram_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
