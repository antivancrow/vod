# Generated by Django 3.1.6 on 2021-02-21 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210221_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='movies.director'),
        ),
    ]
