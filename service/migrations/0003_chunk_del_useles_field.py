# Generated by Django 4.1.2 on 2022-10-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_fie_chunk_index_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filechunk',
            name='path',
        ),
    ]