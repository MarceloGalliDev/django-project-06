# Generated by Django 5.0 on 2024-01-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_pkid"),
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