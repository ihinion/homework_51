# Generated by Django 2.2 on 2020-08-21 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.Project', verbose_name='Project'),
        ),
    ]