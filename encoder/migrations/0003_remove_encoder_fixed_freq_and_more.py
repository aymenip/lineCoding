# Generated by Django 4.0.3 on 2023-01-06 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0002_remove_encoder_scrambling_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encoder',
            name='fixed_freq',
        ),
        migrations.RemoveField(
            model_name='encoder',
            name='fixed_sequence',
        ),
        migrations.RemoveField(
            model_name='encoder',
            name='fixed_size',
        ),
    ]