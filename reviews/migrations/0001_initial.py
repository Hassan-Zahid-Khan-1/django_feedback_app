# Generated by Django 5.1.1 on 2024-09-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.DecimalField(decimal_places=0, max_digits=7)),
                ('student_name', models.TextField(max_length=50)),
                ('student_reviews', models.TextField(max_length=300)),
            ],
        ),
    ]
