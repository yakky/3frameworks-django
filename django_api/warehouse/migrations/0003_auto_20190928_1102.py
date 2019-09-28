# Generated by Django 2.2.5 on 2019-09-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20190928_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf',
            name='available_size',
            field=models.PositiveSmallIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shelf',
            name='size',
            field=models.PositiveSmallIntegerField(editable=False),
        ),
    ]
