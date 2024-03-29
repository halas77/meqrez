# Generated by Django 5.0.2 on 2024-02-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedBackStaffs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.TextField()),
                ("feedback_reply", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="LeaveReportStaff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("leave_date", models.CharField(max_length=255)),
                ("leave_message", models.TextField()),
                ("leave_status", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="NotificationStaffs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Staffs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
