# Generated by Django 4.1.7 on 2023-04-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicum', '0007_alter_answer_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cat',
            field=models.CharField(default=1, max_length=200, verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
