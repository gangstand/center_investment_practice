# Generated by Django 4.1.7 on 2023-04-09 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0009_merge_20230408_2008'),
        ('practicum', '0008_article_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.directionsdesc'),
        ),
    ]
