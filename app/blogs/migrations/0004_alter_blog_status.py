# Generated by Django 4.2.5 on 2023-11-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_blog_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("Draft", "Darft"), ("Published", "Published")],
                default="Draft",
                max_length=20,
            ),
        ),
    ]
