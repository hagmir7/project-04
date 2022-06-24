# Generated by Django 4.0.5 on 2022-06-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_mumbre_membre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evenement',
            old_name='heu',
            new_name='liue',
        ),
        migrations.AlterField(
            model_name='evenement',
            name='image',
            field=models.ImageField(blank=True, default='event.png', null=True, upload_to='EvenementEmage'),
        ),
    ]