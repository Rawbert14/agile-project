# Generated by Django 4.2.5 on 2024-01-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0006_alter_problemreported_problem_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemreported",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
