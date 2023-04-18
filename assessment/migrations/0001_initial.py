# Generated by Django 3.2.10 on 2023-04-18 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_alpha_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_alpha_id', models.CharField(max_length=255, unique=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.object')),
            ],
        ),
    ]