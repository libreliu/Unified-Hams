# Generated by Django 4.0.1 on 2022-01-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(help_text='Datetime for the QSL')),
                ('power', models.FloatField(help_text='Our power used (Watt)', null=True)),
                ('signal_report', models.CharField(help_text='Signal report given by us', max_length=10)),
                ('remote_power', models.FloatField(help_text='Remote power used (Watt)', null=True)),
                ('remote_signal_report', models.CharField(help_text='Signal report given by them', max_length=10)),
            ],
        ),
    ]
