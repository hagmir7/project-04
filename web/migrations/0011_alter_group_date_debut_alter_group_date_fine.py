# Generated by Django 4.0.5 on 2022-06-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_depense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='date_fine',
            field=models.DateField(),
        ),
    ]
