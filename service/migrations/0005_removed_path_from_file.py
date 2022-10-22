# Generated by Django 4.1.2 on 2022-10-21 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0004_file_unique_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filechunk',
            options={'ordering': ['-index']},
        ),
        migrations.RemoveField(
            model_name='uploadedfile',
            name='dir_path',
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
    ]
