# Generated by Django 4.0.2 on 2022-03-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='title',
            field=models.CharField(default='notitle', max_length=255),
        ),
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]