# Generated by Django 3.2.5 on 2021-07-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineasinvestigacionApp', '0002_rename_archivos_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineainvestigacion',
            name='id',
        ),
        migrations.AddField(
            model_name='lineainvestigacion',
            name='id_linea',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]