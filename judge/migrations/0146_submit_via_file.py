# Generated by Django 2.2.24 on 2021-08-23 11:19

import django.db.models.deletion
from django.db import migrations, models

import judge.models.runtime


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0145_alter_problem_pdf_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='file_only',
            field=models.BooleanField(default=False, help_text='If this language is submitted using file or not', verbose_name='File-only language'),
        ),
        migrations.AddField(
            model_name='language',
            name='file_size_limit',
            field=models.IntegerField(blank=True, default=0, help_text='Limit of file size (in MB) if allow submit via file', verbose_name='Limit of file size'),
        ),
        migrations.AlterField(
            model_name='language',
            name='key',
            field=models.CharField(help_text='The identifier for this language; the same as its executor id for judges.', max_length=10, unique=True, verbose_name='short identifier'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.ForeignKey(default=judge.models.runtime.Language.get_default_language_pk, on_delete=django.db.models.deletion.SET_DEFAULT, to='judge.Language', verbose_name='preferred language'),
        ),
    ]