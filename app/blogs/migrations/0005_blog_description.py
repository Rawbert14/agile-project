# Generated by Django 4.2.5 on 2024-01-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_alter_blog_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]