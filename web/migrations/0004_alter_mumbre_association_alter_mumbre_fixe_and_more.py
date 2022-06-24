# Generated by Django 4.0.5 on 2022-06-24 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_rename_nome_mumbre_nom_evenement_heu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mumbre',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.association'),
        ),
        migrations.AlterField(
            model_name='mumbre',
            name='fixe',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mumbre',
            name='photo',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='photos'),
        ),
    ]
