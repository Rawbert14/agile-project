# Generated by Django 4.2.5 on 2024-01-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_quizscore"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quizscore",
            name="score",
            field=models.FloatField(),
        ),
    ]