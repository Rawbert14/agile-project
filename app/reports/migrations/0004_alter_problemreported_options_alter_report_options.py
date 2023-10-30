# Generated by Django 4.2.5 on 2023-10-30 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0003_problemreported"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="problemreported",
            options={
                "verbose_name": "Problem Reported",
                "verbose_name_plural": "Problems Reported",
            },
        ),
        migrations.AlterModelOptions(
            name="report",
            options={"ordering": ("created",)},
        ),
    ]
