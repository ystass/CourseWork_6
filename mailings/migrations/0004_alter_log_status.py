# Generated by Django 5.0.6 on 2024-07-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0003_remove_mailingsettings_client_mailingsettings_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="status",
            field=models.CharField(max_length=30, verbose_name="статус попытки"),
        ),
    ]
