# Generated by Django 5.1.5 on 2025-01-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_attachment_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
