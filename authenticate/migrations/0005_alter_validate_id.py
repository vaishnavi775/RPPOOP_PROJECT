# Generated by Django 4.2 on 2023-05-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_alter_validate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validate',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
