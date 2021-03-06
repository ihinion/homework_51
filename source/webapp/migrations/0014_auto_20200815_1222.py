# Generated by Django 2.2 on 2020-08-15 12:22

from django.db import migrations, models
import webapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, validators=[webapp.validators.restricted_text_art, webapp.validators.no_caps], verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='detailed_desc',
            field=models.TextField(blank=True, max_length=1500, null=True, validators=[webapp.validators.restricted_text_art, webapp.validators.no_caps], verbose_name='Detailed description'),
        ),
    ]
