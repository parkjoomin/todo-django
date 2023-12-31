# Generated by Django 5.0 on 2023-12-27 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=45)),
                ('user_name', models.CharField(max_length=45)),
                ('user_color', models.CharField(blank=True, max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('todo_title', models.CharField(blank=True, max_length=45, null=True)),
                ('todo_content', models.TextField()),
                ('todo_date', models.DateField()),
                ('todo_flag', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
