# Generated by Django 4.0.4 on 2022-07-31 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ziravor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElektronTypeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_uz', models.CharField(max_length=45, verbose_name="O'simlik turi")),
                ('type_ru', models.CharField(max_length=45, verbose_name='Тип ростении')),
            ],
        ),
        migrations.CreateModel(
            name='ElektronModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name_uz', models.CharField(max_length=75, verbose_name='Hujjat nomi')),
                ('file_name_ru', models.CharField(max_length=75, verbose_name='Наименование документа')),
                ('file', models.FileField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ziravor.elektrontypemodels')),
            ],
        ),
    ]
