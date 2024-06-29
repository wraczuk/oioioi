# Generated by Django 4.2.11 on 2024-04-21 12:19

from django.db import migrations
import django.db.models.deletion
import oioioi.participants.fields


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0011_alter_onsiteregistration_participant_and_more'),
        ('mp', '0002_roundscoremultiplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpregistration',
            name='participant',
            field=oioioi.participants.fields.OneToOneBothHandsCascadingParticipantField(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s', to='participants.participant'),
        ),
    ]