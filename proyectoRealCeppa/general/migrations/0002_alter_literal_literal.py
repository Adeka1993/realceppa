# Generated by Django 4.1.2 on 2022-11-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literal',
            name='literal',
            field=models.CharField(max_length=255, verbose_name='Literal'),
        ),
    ]
