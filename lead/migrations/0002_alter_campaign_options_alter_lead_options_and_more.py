# Generated by Django 4.1.3 on 2022-12-02 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'verbose_name_plural': 'Campaign'},
        ),
        migrations.AlterModelOptions(
            name='lead',
            options={'verbose_name_plural': 'Leads'},
        ),
        migrations.RemoveField(
            model_name='lead',
            name='agent_name',
        ),
    ]