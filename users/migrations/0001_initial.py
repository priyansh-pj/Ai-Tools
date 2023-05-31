# Generated by Django 4.2.1 on 2023-05-31 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(max_length=250)),
                ("first_name", models.CharField(blank=True, max_length=200, null=True)),
                ("last_name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.CharField(max_length=400)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                ("short_intro", models.TextField(blank=True, null=True)),
                ("bio", models.TextField()),
                (
                    "social_github",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_twitter",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_website",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
