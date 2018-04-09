# Generated by Django 2.0.3 on 2018-04-09 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('devices', '0003_auto_20180409_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='attributesId',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='attributesType',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
    ]
