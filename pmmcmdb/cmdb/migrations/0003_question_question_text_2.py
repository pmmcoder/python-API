# Generated by Django 2.0.6 on 2008-12-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180627_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text_2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
