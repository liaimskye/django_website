# Generated by Django 3.2.18 on 2023-04-10 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20230410_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]