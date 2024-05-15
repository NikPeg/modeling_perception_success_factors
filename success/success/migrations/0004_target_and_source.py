# Generated by Django 5.0.3 on 2024-05-12 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0003_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='source',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='source_links', to='success.factor'),
        ),
        migrations.AddField(
            model_name='link',
            name='target',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='target_links', to='success.factor'),
        ),
    ]