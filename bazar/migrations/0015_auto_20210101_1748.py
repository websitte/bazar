# Generated by Django 3.1.4 on 2021-01-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0014_auto_20210101_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polozky',
            name='mesto',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='polozky',
            name='popis',
            field=models.TextField(),
        ),
    ]
