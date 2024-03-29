# Generated by Django 5.0.2 on 2024-02-26 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0002_initial"),
        ("students", "0001_initial"),
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="session_year_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.sessionyearmodel"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="subject_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="courses.subjects"
            ),
        ),
        migrations.AddField(
            model_name="attendancereport",
            name="attendance_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.attendance"
            ),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="subject_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.subjects",
            ),
        ),
        migrations.AddField(
            model_name="students",
            name="admin",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="students",
            name="course_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="courses.courses",
            ),
        ),
        migrations.AddField(
            model_name="students",
            name="session_year_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.sessionyearmodel",
            ),
        ),
        migrations.AddField(
            model_name="studentresult",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.students"
            ),
        ),
        migrations.AddField(
            model_name="notificationstudent",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.students"
            ),
        ),
        migrations.AddField(
            model_name="leavereportstudent",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.students"
            ),
        ),
        migrations.AddField(
            model_name="feedbackstudent",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="students.students"
            ),
        ),
        migrations.AddField(
            model_name="attendancereport",
            name="student_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="students.students"
            ),
        ),
    ]
