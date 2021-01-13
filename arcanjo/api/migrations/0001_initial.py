# Generated by Django 2.2.6 on 2019-10-19 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('bithday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('guardian_name', models.CharField(max_length=200)),
                ('ts_opening', models.DateTimeField(auto_now_add=True)),
                ('ts_checkin', models.DateTimeField(blank=True, default=None, null=True)),
                ('ts_sorting', models.DateTimeField(blank=True, default=None, null=True)),
                ('ts_consultation_start', models.DateTimeField(blank=True, default=None, null=True)),
                ('ts_consultation_end', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='PatientSymptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Patient')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Session')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Symptom')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('step', models.IntegerField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Session')),
            ],
        ),
    ]