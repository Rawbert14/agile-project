# Generated by Django 4.2.5 on 2024-01-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0010_alter_report_end_hour_alter_report_start_hour"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
