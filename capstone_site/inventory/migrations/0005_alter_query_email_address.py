# Generated by Django 3.2.18 on 2023-04-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20230410_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
