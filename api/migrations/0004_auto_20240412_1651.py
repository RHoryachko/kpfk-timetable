# Generated by Django 3.2.23 on 2024-04-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20240412_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='numerator',
            field=models.CharField(choices=[('чисельник', 'Чисельник'), ('знаменник', 'Знаменник')], max_length=20),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='room',
            field=models.IntegerField(),
        ),
    ]
