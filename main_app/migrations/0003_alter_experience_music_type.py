# Generated by Django 4.1.6 on 2023-02-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_experience_show_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='music_type',
            field=models.CharField(blank=True, choices=[('AL', 'ALBUM'), ('SI', 'Single'), ('MI', 'Mixtape'), ('EP', 'EP'), ('FE', 'Features On')], max_length=2, null=True),
        ),
    ]
