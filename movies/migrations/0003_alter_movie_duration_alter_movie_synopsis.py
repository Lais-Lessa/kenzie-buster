# Generated by Django 4.2.5 on 2023-10-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(blank=True, default=''),
        ),
    ]
