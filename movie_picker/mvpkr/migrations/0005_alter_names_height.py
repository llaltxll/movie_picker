# Generated by Django 4.0 on 2021-12-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvpkr', '0004_alter_names_children_alter_names_date_of_death_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='names',
            name='height',
            field=models.IntegerField(null=True),
        ),
    ]
