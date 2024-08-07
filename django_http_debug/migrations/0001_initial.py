# Generated by Django 5.0.2 on 2024-08-07 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DebugEndpoint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=255, unique=True)),
                ("status_code", models.IntegerField(default=200)),
                ("headers", models.JSONField(blank=True, default=dict)),
                ("content", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="RequestLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("method", models.CharField(max_length=10)),
                ("headers", models.JSONField()),
                ("body", models.TextField(blank=True)),
                ("is_base64", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "endpoint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_http_debug.debugendpoint",
                    ),
                ),
            ],
        ),
    ]