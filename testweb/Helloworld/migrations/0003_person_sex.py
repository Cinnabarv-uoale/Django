# Generated by Django 5.1 on 2024-08-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Helloworld", "0002_student_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="sex",
            field=models.CharField(default=1, max_length=2, verbose_name="性别"),
            preserve_default=False,
        ),
    ]
