# Generated by Django 3.2.13 on 2022-06-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djflights', '0006_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]