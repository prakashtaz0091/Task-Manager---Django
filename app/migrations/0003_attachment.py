# Generated by Django 5.1.5 on 2025-01-21 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task')),
            ],
        ),
    ]
