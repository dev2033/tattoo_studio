# Generated by Django 3.2.4 on 2021-06-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20210614_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-id'], 'verbose_name': 'Татуировку', 'verbose_name_plural': 'Татуировки'},
        ),
    ]
