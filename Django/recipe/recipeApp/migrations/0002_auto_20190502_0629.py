# Generated by Django 2.1.7 on 2019-05-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='CaloriesServing',
            field=models.FloatField(blank=True, null=True),
        ),
    ]