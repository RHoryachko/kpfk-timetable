# Generated by Django 3.2.23 on 2024-04-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20240412_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_number',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1),
            preserve_default=False,
        ),
    ]
