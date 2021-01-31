# Generated by Django 3.1.4 on 2020-12-25 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0003_auto_20201225_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategorieBazaru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='city',
            new_name='cena',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='price',
            new_name='mesto',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='title',
            new_name='nazev',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='text',
            new_name='popis',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='published_date',
            new_name='publikovano',
        ),
        migrations.RenameField(
            model_name='polozkabazaru',
            old_name='created_date',
            new_name='vytvoreno',
        ),
        migrations.AddField(
            model_name='polozkabazaru',
            name='kategorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bazar.kategoriebazaru'),
        ),
    ]
