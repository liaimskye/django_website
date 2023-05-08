# Generated by Django 3.2.18 on 2023-04-10 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='email_address',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='query',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
    ]