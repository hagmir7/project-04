# Generated by Django 4.0.5 on 2022-06-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_rename_heu_evenement_liue_alter_evenement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='douateurass',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='douateurass',
            name='montant',
            field=models.FloatField(default=0),
        ),
    ]