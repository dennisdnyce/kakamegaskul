# Generated by Django 3.0.4 on 2020-03-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0003_auto_20200320_0811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school_core_values',
            options={'verbose_name': 'school Core Value', 'verbose_name_plural': 'school Core Values'},
        ),
        migrations.RenameField(
            model_name='school_core_values',
            old_name='core_value_five',
            new_name='core_value',
        ),
        migrations.RemoveField(
            model_name='school_core_values',
            name='core_value_four',
        ),
        migrations.RemoveField(
            model_name='school_core_values',
            name='core_value_one',
        ),
        migrations.RemoveField(
            model_name='school_core_values',
            name='core_value_three',
        ),
        migrations.RemoveField(
            model_name='school_core_values',
            name='core_value_two',
        ),
    ]
