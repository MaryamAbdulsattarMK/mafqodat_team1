# Generated by Django 4.1.5 on 2023-02-13 11:10

import Todo.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(default='Iraq', max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PostTimeDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expierd_at', models.DateTimeField(default=Todo.models.in_three_days)),
                ('edits_time', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Type_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=255)),
                ('city', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='Todo.location')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Date', models.DateField(auto_created=True, default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=250)),
                ('image', models.ImageField(default='default/1.png', upload_to='photo/%y/%m/%d')),
                ('phone_number', models.IntegerField(default=12345)),
                ('chat_count', models.IntegerField(default=1)),
                ('Action', models.TextField(default='default')),
                ('is_checked_by_admin', models.BooleanField(default=False)),
                ('PostDetail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Todo.posttimedetail')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todo.regions')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Todo.type_item')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]