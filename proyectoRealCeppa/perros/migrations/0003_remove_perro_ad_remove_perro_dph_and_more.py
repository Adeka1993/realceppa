# Generated by Django 4.1.2 on 2022-11-06 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0002_prueba_alter_loperro_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perro',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='dph',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='fechaBH',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='fechaTS',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='fechaTU',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='fhmax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='fpr',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='gradoMax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='hgh',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='ipmax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='phmax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='pshmax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='rhmax',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='rtp',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='stp',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='tsi',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='wh',
        ),
        migrations.RemoveField(
            model_name='perro',
            name='zhmax',
        ),
    ]
