# Generated by Django 3.1.5 on 2022-05-26 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0003_auto_20220525_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='hospital_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]