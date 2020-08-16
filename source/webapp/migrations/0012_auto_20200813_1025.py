# Generated by Django 2.2 on 2020-08-13 10:25

from django.db import migrations, models
import webapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200811_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, validators=[webapp.validators.restricted_text_art, webapp.validators.min_30, webapp.validators.no_caps], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='detailed_desc',
            field=models.TextField(blank=True, max_length=1500, null=True, validators=[webapp.validators.at_least_200, webapp.validators.restricted_text_art, webapp.validators.no_caps], verbose_name='Detailed description'),
        ),
    ]