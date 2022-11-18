# Generated by Django 4.1.2 on 2022-10-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mini_desc', models.TextField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(max_length=1000)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('teacher', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
                ('last_name', models.CharField(default='None', max_length=100)),
                ('id_number', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mini_desc', models.TextField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(max_length=1000)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(blank=True, default=0, null=True)),
                ('teacher', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='online.lessons')),
            ],
        ),
    ]
