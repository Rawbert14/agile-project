# Generated by Django 4.2.5 on 2023-11-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(max_length=300),
        ),
    ]
