# Generated by Django 4.2.6 on 2023-10-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outage', '0002_rename_pt33kv11kvparent_gistransmissionsubstations_powertrans'),
    ]

    operations = [
        migrations.AddField(
            model_name='gisfeeders',
            name='Tech_engineer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gisfeeders',
            name='Tech_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gisfeeders',
            name='Tech_supervisor',
            field=models.BooleanField(default=False),
        ),
    ]
