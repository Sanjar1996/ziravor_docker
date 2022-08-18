# Generated by Django 4.0.4 on 2022-07-31 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('sub_title_uz', models.CharField(max_length=255)),
                ('sub_title_ru', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FloraTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_uz', models.CharField(max_length=45)),
                ('type_ru', models.CharField(max_length=45)),
                ('type_en', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='XodimModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_uz', models.CharField(max_length=255)),
                ('fullname_ru', models.CharField(max_length=255)),
                ('lavozim_uz', models.CharField(max_length=255)),
                ('lavozim_ru', models.CharField(max_length=255)),
                ('qabul_uz', models.CharField(max_length=255)),
                ('qabul_ru', models.CharField(max_length=255)),
                ('brith_day', models.DateField(blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('telegram', models.CharField(blank=True, max_length=255)),
                ('tel_raqam', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='YangiliklarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title_uz', models.CharField(max_length=255)),
                ('sub_title_ru', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('text_uz', models.TextField()),
                ('text_ru', models.TextField()),
                ('data', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FloraModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=45)),
                ('name_ru', models.CharField(max_length=45)),
                ('title_uz', models.CharField(max_length=100)),
                ('title_ru', models.CharField(max_length=100)),
                ('subtitle_uz', models.CharField(max_length=255)),
                ('subtitle_ru', models.CharField(max_length=255)),
                ('info_uz', models.TextField()),
                ('info_ru', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('data', models.DateTimeField(blank=True)),
                ('flora_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ziravor.floratypemodel')),
            ],
        ),
    ]
