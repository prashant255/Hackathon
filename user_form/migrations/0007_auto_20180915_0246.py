# Generated by Django 2.1.1 on 2018-09-15 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_form', '0006_auto_20180913_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]