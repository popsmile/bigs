# Generated by Django 2.0.7 on 2018-08-02 02:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20180802_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcard',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
