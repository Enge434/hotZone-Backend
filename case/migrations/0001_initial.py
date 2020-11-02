# Generated by Django 3.1.2 on 2020-11-02 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('virus', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=20)),
                ('date_confirmed', models.IntegerField()),
                ('local_or_imported', models.CharField(choices=[('Local', 'local'), ('Imported', 'imported')], default='Local', max_length=10)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('virus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virus.virus')),
            ],
        ),
    ]