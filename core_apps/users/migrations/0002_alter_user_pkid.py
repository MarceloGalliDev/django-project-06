# Generated by Django 5.0 on 2024-01-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="pkid",
            field=models.BigIntegerField(
                editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
