# Generated by Django 4.2.5 on 2023-10-30 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0004_alter_problemreported_options_alter_report_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="report",
            options={"ordering": ("-created",)},
        ),
        migrations.AddField(
            model_name="problemreported",
            name="report",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="reports.report",
            ),
            preserve_default=False,
        ),
    ]
