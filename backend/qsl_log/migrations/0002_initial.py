# Generated by Django 4.0.1 on 2022-01-25 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qsl_log', '0001_initial'),
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='antenna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='log_entry_as_home', to='station.antenna'),
        ),
    ]