# Generated by Django 4.2.3 on 2023-08-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
