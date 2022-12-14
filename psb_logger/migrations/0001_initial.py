# Generated by Django 4.1.3 on 2022-11-05 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build', models.CharField(max_length=10, verbose_name='build')),
                ('task', models.CharField(max_length=25, verbose_name='task')),
                ('database', models.CharField(max_length=15, verbose_name='database')),
                ('hash', models.CharField(max_length=255, verbose_name='hash')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('date', models.DateTimeField()),
                ('message', models.TextField(verbose_name='message')),
                ('filename', models.TextField(verbose_name='filename')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'maintable',
            },
        ),
    ]
