# Generated by Django 4.1.7 on 2023-04-08 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practicum', '0004_quiz_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='difficluty',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='number_of_questions',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='required_score_to_pass',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='time',
        ),
    ]
