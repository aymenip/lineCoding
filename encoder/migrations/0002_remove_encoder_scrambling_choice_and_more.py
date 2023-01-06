# Generated by Django 4.0.3 on 2023-01-06 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encoder',
            name='scrambling_choice',
        ),
        migrations.AlterField(
            model_name='encoder',
            name='bit_size',
            field=models.IntegerField(blank=True, default=3),
        ),
        migrations.AlterField(
            model_name='encoder',
            name='scheme_choice',
            field=models.CharField(choices=[('Unipolar', 'Unipolar'), ('NRZ-L', 'NRZ-L'), ('NRZ-I', 'NRZ-I'), ('Polar RZ', 'Polar RZ'), ('Unipolar RZ', 'Unipolar RZ'), ('Manchester', 'Manchester'), ('Differential Manchester', 'Differential Manchester'), ('AMI', 'AMI')], default='Unipolar', max_length=50),
        ),
    ]
