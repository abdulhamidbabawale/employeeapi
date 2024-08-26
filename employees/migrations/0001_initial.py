# Generated by Django 5.1 on 2024-08-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employees",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("position", models.CharField(max_length=200)),
                ("department", models.CharField(max_length=200)),
                ("employee_email", models.EmailField(max_length=200)),
                ("performance_review", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True)),
                ("joined_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]