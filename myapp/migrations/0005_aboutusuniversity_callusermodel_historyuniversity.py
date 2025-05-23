# Generated by Django 5.2 on 2025-04-21 08:03

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_rektoratcategory_name_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=450, verbose_name='sarlovha')),
                ('name_uz', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('name_en', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('name_ru', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('body', models.TextField(blank=True, default='hozircha malumot yoq')),
                ('body_uz', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('body_en', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('body_ru', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('photo', models.ImageField(upload_to='media/about-us')),
            ],
            options={
                'verbose_name': 'Universitet Haqida',
                'verbose_name_plural': 'Universitet haqida',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CallUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='F.I.SH')),
                ('name_uz', models.CharField(max_length=150, null=True, verbose_name='F.I.SH')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='F.I.SH')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='F.I.SH')),
                ('body', models.TextField(verbose_name='Malumot')),
                ('body_uz', models.TextField(null=True, verbose_name='Malumot')),
                ('body_en', models.TextField(null=True, verbose_name='Malumot')),
                ('body_ru', models.TextField(null=True, verbose_name='Malumot')),
                ('rang', models.CharField(max_length=150, verbose_name='lavozim')),
                ('rang_uz', models.CharField(max_length=150, null=True, verbose_name='lavozim')),
                ('rang_en', models.CharField(max_length=150, null=True, verbose_name='lavozim')),
                ('rang_ru', models.CharField(max_length=150, null=True, verbose_name='lavozim')),
                ('qabul_day', models.CharField(blank=True, max_length=150, verbose_name='qabul kuni')),
                ('qabul_day_uz', models.CharField(blank=True, max_length=150, null=True, verbose_name='qabul kuni')),
                ('qabul_day_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='qabul kuni')),
                ('qabul_day_ru', models.CharField(blank=True, max_length=150, null=True, verbose_name='qabul kuni')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Tell number')),
                ('photo', models.ImageField(upload_to='media/call')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Aloqa Hodimi',
                'verbose_name_plural': 'Aloqa Hodimi',
            },
        ),
        migrations.CreateModel(
            name='HistoryUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=450, verbose_name='sarlovha')),
                ('name_uz', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('name_en', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('name_ru', models.CharField(max_length=450, null=True, verbose_name='sarlovha')),
                ('body', models.TextField(blank=True, default='hozircha malumot yoq')),
                ('body_uz', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('body_en', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('body_ru', models.TextField(blank=True, default='hozircha malumot yoq', null=True)),
                ('photo', models.ImageField(upload_to='media/about-us')),
            ],
            options={
                'verbose_name': 'Universitet Tarixi',
                'verbose_name_plural': 'Universitet Tarixi',
                'ordering': ['-id'],
            },
        ),
    ]
