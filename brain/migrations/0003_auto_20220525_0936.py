# Generated by Django 3.1.5 on 2022-05-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0002_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='story',
            name='story',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='story',
            name='storytitle',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='story',
            name='type',
            field=models.CharField(max_length=200),
        ),
    ]
