# Generated by Django 3.1.7 on 2021-03-23 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('status', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('url', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('separator', models.CharField(blank=True, max_length=10, null=True)),
                ('string_char', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=80)),
                ('order', models.IntegerField()),
                ('range_min', models.IntegerField(blank=True, default=0)),
                ('range_max', models.IntegerField(blank=True, default=0)),
                ('data_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas.datatype')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column', to='schemas.schema')),
            ],
            options={
                'unique_together': {('schema', 'order')},
            },
        ),
    ]
