# Generated by Django 4.2.11 on 2024-03-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
