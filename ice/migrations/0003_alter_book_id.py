# Generated by Django 3.2 on 2021-12-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice', '0002_rename_ice_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
