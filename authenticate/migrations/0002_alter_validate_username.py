# Generated by Django 4.2 on 2023-05-18 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validate',
            name='username',
            field=models.CharField(max_length=122),
        ),
    ]
