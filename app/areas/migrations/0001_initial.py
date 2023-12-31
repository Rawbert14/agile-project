# Generated by Django 4.2.5 on 2023-10-29 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0002_alter_profile_profile_picture"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductionLine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("products", models.ManyToManyField(to="products.product")),
                (
                    "team_leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.profile",
                    ),
                ),
            ],
        ),
    ]
