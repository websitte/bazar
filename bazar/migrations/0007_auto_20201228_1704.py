# Generated by Django 3.1.4 on 2020-12-28 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0006_auto_20201228_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypInzeratu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='polozkabazaru',
            name='typ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bazar.typinzeratu'),
        ),
    ]
